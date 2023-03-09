from django import template

register = template.Library()

@register.filter("windownum")
def window_num(foodID):
    return int(foodID/100%100)
register.filter("windownum", window_num)



