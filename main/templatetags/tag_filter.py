from django import template

register = template.Library()

@register.filter()
def my_filter(val):
    if val:
        return val

    return '#'
