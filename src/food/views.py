from django.shortcuts import render
from .models import food
from comment.models import comment
from django.core.paginator import Paginator
from index.views import check_login
# Create your views here.
@check_login
def food_view(request, foodnum):
    getfood = food.objects.get(foodID=foodnum)
    
    comment_list = comment.objects.filter(food=getfood)
    
    stars_cnt = 0.0
    
    for c in comment_list:
        stars_cnt += c.stars
    
    comment_num = len(comment_list)
    
    if comment_num !=0:
        stars_avg = stars_cnt / comment_num
    else:
        stars_avg = 0
    
    stars_avg = round(stars_avg,2)
    
    getfood.stars = stars_avg
    
    getfood.save();
    
    paginator = Paginator(comment_list, 7) # Show 20 food per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'food/food.html', locals())