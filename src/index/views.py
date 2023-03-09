from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from food.models import food
from django.db.models import Q
from django.core.paginator import Paginator
from comment.models import comment
from user.models import User
import os
# Create your views here.
def check_login(fn):
    def wrap(request, *args, **kwargs):
        if 'username' not in request.session:
            c_username = request.COOKIES.get('username')
            if not c_username:
                return HttpResponseRedirect('/index')
            else:
                request.session['username'] = c_username
        
        return fn(request, *args, **kwargs)
    return wrap
def index_view(request):
    
    return render(request, 'index/index.html')

@check_login
def search_view(request):
    search = request.GET.get('searchs')
    if not search:
        food_list = []
    else:
        food_list = food.objects.filter(Q(foodID__icontains=search)|Q(name__icontains=search))
    res_num = len(food_list)
    
    paginator = Paginator(food_list, 10) # Show 20 food per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index/search.html', locals())

@check_login
def top_view(request):
    restaurant_id = request.GET.get('q',"0")

    if restaurant_id == "0":
        food_list = food.objects.all().order_by('-stars')
    else :
        food_list = food.objects.filter(foodID__startswith=restaurant_id).order_by('-stars')
    with open(os.path.dirname(os.path.abspath(__file__))+"/static/top/top"+restaurant_id+".txt","w") as f:
        if len(food_list) == 0:
            s = ""
            f.write(s)
        else :
            for i in range(0,9):
                if i < len(food_list):
                    s = "<div class=\"wrapper pad_bot2\">\
                  <div class=\"results-message\">\
                  </div>\
                  <div class=\"flex-row justify-content-flex-start\">\
                    <div class=\"image-container\">\
                        <img src=\"/static/images/"+ str(food_list[i].foodID)+".jpg\"\
                        width=\"200px\" height=\"200px\"  >\
                    </div>\
                  </div>\
                      <p class=\"pad_bot1\">\
                    <strong>食堂名称</strong>:"+ str(foodid2(food_list[i].foodID))+"<br />\
                    <strong>窗口号</strong>:"+ str(int(food_list[i].foodID/100%100))+"<br />\
                    <strong>餐品名称</strong>:<a href=\"/food/"+str(food_list[i].foodID)+"\">"+str(food_list[i].name)+"</a><br/>\
                    <strong >辣度</strong>:"+ str(spiciness2(food_list[i].spiciness))+"<br>\
                    <strong>价格</strong>:"+str(food_list[i].price)+"<br />\
                    <strong>评分</strong>:"+str(food_list[i].stars)+"<br />\
                    <br />\
                    <br /></p>\</div>"
                    f.write(s)
    
    
    
    return render(request, 'index/top.html', locals())

@check_login
def sift_view(request):
    place = request.GET.get('place')
    price = request.GET.get('price')
    c_spiciness = request.GET.get('spiciness')
    specialfood = request.GET.get('specialfood')

    if not place:
        place='0'
    if not specialfood:
        specialfood='0'
    if not c_spiciness:
        c_spiciness = '0'

       

    if place!='0':
        food_list=food.objects.filter(Q(foodID__startswith=place))
    else:
        food_list=food.objects.all()

    if c_spiciness!='0':
        food_list = food_list.filter(spiciness=c_spiciness)
    else:
        food_list=food_list.all()

    if specialfood == '0':
        food_list = food_list
    else:
        food_list = food.objects.filter(Q(name__exact=specialfood))
        
    res_num = len(food_list)

    paginator = Paginator(food_list, 1)  # Show 20 food per page.

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    return render(request, 'index/sift.html',locals())

@check_login
def latest_view(request):
    
    comment_list = comment.objects.all()
    comment_list = comment.objects.order_by('-created_time')
    
    paginator = Paginator(comment_list, 7) # Show 20 food per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) 


    return render(request, 'index/latest.html',locals())

@check_login
def remark_view(request):
    if request.method=='GET':
         canteen_num=-1
         return render(request,'index/remark.html',locals())
    if request.method == 'POST':
        canteen_num=int(request.POST.get('canteen'))
        window_num=int(request.POST.get('window'))
        food_num=int(request.POST.get('food'))
        stars=float(request.POST.get('starLevel'))
        content=request.POST.get('textarea')
        foodid=(canteen_num+1)*100000+10000+(window_num+1)*100+food_num+1
        uname = request.session['username']
        user = User.objects.get(username=uname)
        get_food = food.objects.get(foodID=foodid)
        comment.objects.create(content=content, stars=stars, user=user, food=get_food)
        return render(request, 'index/index.html',locals())

def foodid2(foodID):
    restaurant_list = ['第一餐饮大楼','第二餐饮大楼','第三餐饮大楼','第四餐饮大楼','第五餐饮大楼','第六餐饮大楼','第七餐饮大楼',
                       '玉兰苑','哈乐餐厅']
    restaurant = restaurant_list[int(foodID/100000) - 1]
    return restaurant

def spiciness2(num):
    spiciness_list = ['不辣', '微辣','辣','很辣']
    spiciness = spiciness_list[num - 1]
    return spiciness