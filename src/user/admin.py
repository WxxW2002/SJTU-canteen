from django.contrib import admin
from .models import User
# Register your models here.

class User_display(admin.ModelAdmin):
    list_display=['username','password','create_time','update_time']

admin.site.register(User,User_display)
#后台管理展示的属性