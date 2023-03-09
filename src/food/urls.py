from . import views
from django.urls import path

urlpatterns = [
    
    path('<int:foodnum>', views.food_view)
]