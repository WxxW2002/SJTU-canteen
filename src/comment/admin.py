from django.contrib import admin
from .models import comment
# Register your models here.

class comment_display (admin.ModelAdmin):
    list_display=['content','stars','created_time','updated_time','user','food','likes','unlikes']
    list_display_link=['content']
    list_filter=['stars','created_time']
    search_fields=['food']
#后台管理展示的属性    
    
admin.site.register(comment,comment_display)