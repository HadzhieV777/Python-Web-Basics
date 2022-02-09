from django import template

register = template.Library()


@register.filter(name='increase_by')
def increase_by(value, number):
    return value + number
