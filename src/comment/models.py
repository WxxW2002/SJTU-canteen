from django.db import models
from user.models import User
from food.models import food
# Create your models here.
class comment(models.Model):
    content = models.TextField('content')
    stars = models.IntegerField('stars', default=0)
    created_time = models.DateTimeField('created_time', auto_now_add=True)
    updated_time = models.DateTimeField('updated_time', auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(food, on_delete=models.CASCADE, default="")
    likes = models.IntegerField('Likes', default = 0)
    unlikes = models.IntegerField('Unlikes', default = 0)

    