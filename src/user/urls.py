from . import views

from django.urls import path

urlpatterns = [
    path('reg', views.reg_view), #注册
    path('login', views.login_view), #登陆
    path('logout', views.logout_view), #登出
    path('info', views.user_info),#用户页面
    path('changename',views.user_changename),#改名
#    path('comments',views.comments),
#    path('instructions',views.instructions),
#    path('update_comments/<int:fdID>',views.update_comments),
#    path('delete/<int:fdID>',views.delete),
#    path('update_instructions',views.update_instructions),
]