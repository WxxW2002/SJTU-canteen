from django import template

register = template.Library()


@register.filter("spiciness")
def spiciness_num(num):
    return spiciness2(num)
register.filter("spiciness", spiciness_num)


def spiciness2(num):
    spiciness_list = ['不辣', '微辣','辣','很辣']
    spiciness = spiciness_list[num - 1]
    return spiciness