from django.db import models
# Create your models here.
class User(models.Model):
    
    username = models.CharField("username", max_length=30, unique=True)
    password = models.CharField("password", max_length=32)
    create_time = models.DateTimeField("create_time", auto_now_add=True)
    update_time = models.DateTimeField("update_time", auto_now=True)
    
#用户数据库