from . import views
from django.urls import path

urlpatterns = [
    path('<int:foodnum>', views.comment_view),
    path('like/<int:commentid>', views.Like_view)
]