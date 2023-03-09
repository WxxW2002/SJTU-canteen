from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from food.models import food
from user.models import User
from .models import comment
from index.views import check_login
# Create your views here.
@check_login
def comment_view(request, foodnum):
    if request.method == 'GET':
        get_food = food.objects.get(foodID=foodnum)
        if not get_food:
            return HttpResponse("food not exist")
    
        return render(request, 'comment/comment.html', locals())

    elif request.method == 'POST':
        
        uname = request.session['username']
        user = User.objects.get(username=uname)
        content = request.POST['comment']
        stars = float(request.POST['stars'])
        get_food = food.objects.get(foodID=foodnum)
        comment.objects.create(content=content, stars=stars, user=user, food = get_food)
        
        #from django.urls import reverse
        #url = reverse('food:foodnum', kwargs={'foodnum':get_food.foodID})
        urll = '/food/'+str(foodnum)
        return HttpResponseRedirect(urll)
    

@check_login
def Like_view(request, commentid):
    c_comment = comment.objects.get(id=commentid)
    
    likenum = request.GET['likenum']
    
    c_comment.likes = likenum
    c_comment.save()
    return HttpResponse('good')