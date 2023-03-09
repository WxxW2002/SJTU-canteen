from django.contrib import admin
from .models import food
# Register your models here.

class food_display(admin.ModelAdmin):
    list_display=['foodID','name','stars','price']
#后台管理展示的属性
admin.site.register(food,food_display)