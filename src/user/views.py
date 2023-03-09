from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from user.models import User
import hashlib
from food.models import food
from comment.models import comment
# Create your views here.
def reg_view(request):
# 注册页面    
    if request.method =='GET':
        return render(request, 'user/register.html')
    elif request.method =='POST':
        username = request.POST['username']
        password_1 = request.POST['password_1']
        password_2 = request.POST['password_2']
        
        if password_1 != password_2:
            return HttpResponse('password again must be equal to password')
#判断两次输入的密码是否一致       
        m = hashlib.md5()
        m.update(password_1.encode())
        password_m = m.hexdigest()
#对密码加密        
        
        old_users = User.objects.filter(username=username)
        if old_users:
            return HttpResponse('invalid username')
        try:
            user = User.objects.create(username=username, password=password_m)
        except Exception as e:
            print('invalid username')
            return  HttpResponse('invalid username')
#存入数据库        
        request.session['username'] = username

        return HttpResponseRedirect('/index')


def login_view(request):
#登录界面
    if request.method == 'GET':
        if request.session.get('username'):
            return HttpResponseRedirect('/index')
        
        c_username = request.COOKIES.get('username')
        if c_username :
            request.session['username'] = c_username
            return HttpResponseRedirect('/index')
        
        
        return render(request, 'user/login.html')
    elif request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = User.objects.get(username=username)
        except Exception as e:
            print('--login user error %s'%(e))
            return HttpResponse('username error')
#检查用户名        
        m = hashlib.md5()
        m.update(password.encode())
        if m.hexdigest() != user.password:
            return HttpResponse('password error')
#检查密码        
        request.session['username'] = username
        
        resp = HttpResponseRedirect('/index')
        
        if 'remember' in request.POST:
            resp.set_cookie('username', username, 3600*24*2)
            
        return  resp 

def logout_view(request):
    if 'username' in request.session:
        del request.session['username']
    
    resp = HttpResponseRedirect('/index')
    if 'username' in request.COOKIES:
        resp.delete_cookie('username')
    
    return resp
#以下被废弃
#def user_info(request):
    #用户界面主界面
    tmp=request.session.get('username','')
    myuser=User.objects.get(username=tmp)
    return render(request,'user/instructions.html',locals())
#def comments(request):
    #用户评论主界面
    tmp=request.session.get('username','')
    myuser=User.objects.get(username=tmp)
    all_comments=comment.objects.filter(user=myuser)
    return render(request,'user/comments.html',locals())
#def instructions(request):
    #用户信息主界面
    tmp=request.session.get('username','')
    myuser=User.objects.get(username=tmp)
    return render(request,'user/instructions.html',locals())

def user_info(request):
    tmp=request.session.get('username')
    myuser=User.objects.get(username=tmp)
    control=0    #控制异常
    if request.method=='GET':
       control=0
       return render(request,'user/user_info.html',locals())
    elif request.method=='POST':
        oldpassword=request.POST['oldPassword']
        newpassword=request.POST['newPassword']
        confirm=request.POST['confirm']
        m = hashlib.md5()
        m.update(oldpassword.encode())
        if m.hexdigest() != myuser.password:
            control= 1   #原密码不对
            return render(request,'user/user_info.html',locals())
        elif confirm != newpassword:
            control = 2    #密码不一样
            return render(request,'user/user_info.html',locals())
        else: 
            control = 0            
            m = hashlib.md5()
            m.update(newpassword.encode())
            newpassword_m = m.hexdigest()
            myuser.password=newpassword_m
            myuser.save()
            return render(request,'user/success.html',locals())
        
def user_changename(request):
    tmp=request.session.get('username','')
    myuser=User.objects.get(username=tmp)
    newname=request.POST['nickname']
    repeat=0 #控制重名
    all_names=User.objects.values('username')
    for name in all_names:
        if name['username']==newname:
            repeat=1
            break
    if repeat ==0:
        myuser.username=newname
        myuser.save()
        request.session['username']=newname
        request.COOKIES['username']=newname
        return render(request,'user/success.html')
    else:
        return render(request,'user/user_info.html',locals())

#def update_comments(request,fdID):
    #更新评论主界面
    try:
        tmp=request.session.get('username','')
        myuser=User.objects.get(username=tmp)
        myfood=food.objects.get(foodID=fdID)
        comments=comment.objects.get(user=myuser,food=myfood)
        
        
    #找到该评论
    except Exception as e:
        print('%s is not exist.'%e)
        return HttpResponse('Not exist')
    
    if request.method == 'GET':
        return render(request,'user/update_comments.html',locals())
    #原页面
    elif request.method =='POST':
        newcomment=request.POST['newcomment']
        comments.content=newcomment
        comments.save()
        return HttpResponseRedirect('/user/comments')
            
#def delete(request,fdID):
    if not fdID:
        return HttpResponse('请求异常')
    try:
        myfood=food.objects.get(foodID=fdID)
        tmp=request.session.get('username','')
        myuser=User.objects.get(username=tmp)
        mycomment=comment.objects.get(user=myuser,food=myfood)
    except Exception as e:
        print('error')
        return HttpResponse('error')
    mycomment.delete()
    return HttpResponseRedirect('/user/comments')
    
     