from django import template

register = template.Library()

@register.filter("restaurant")
def restaurant_name(foodID):
    
    return foodid2(foodID)
register.filter("restaurant", restaurant_name)

def foodid2(foodID):
    restaurant_list = ['第一餐饮大楼','第二餐饮大楼','第三餐饮大楼','第四餐饮大楼','第五餐饮大楼','第六餐饮大楼','第七餐饮大楼',
                       '玉兰苑','哈乐餐厅']
    restaurant = restaurant_list[int(foodID/100000) - 1]
    return restaurant