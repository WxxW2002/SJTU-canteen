from . import views
from django.urls import path

urlpatterns = [
    path('', views.index_view), 
    path('search', views.search_view),
    path('top', views.top_view),
    path('sift', views.sift_view),
    path('latest', views.latest_view),
    path('remark',views.remark_view)
]