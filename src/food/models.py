from django.db import models

# Create your models here.
class food(models.Model):
    foodID = models.IntegerField('foodID', primary_key=True)  #6位
    #第一位表示餐厅 1：一餐 2 ：二餐。。。 7：七餐 8 ：玉兰苑 9：哈乐
    #第二位表示餐厅层数
    #第三、四位表示窗口号
    #第五、第六位表示food号
    #这样foodID唯一 
    name = models.CharField('name', max_length=20)
    price = models.DecimalField('price', max_digits=7, decimal_places=2)
    stars = models.DecimalField('stars', max_digits=3, decimal_places=1, default=0)
    spiciness = models.IntegerField('spiciness', default=1)
    # 1 不辣  2 微辣 3 很辣 4 变态辣
    
    def __str__(self):
        return '%s'%(self.name)