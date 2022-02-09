from django import template

register = template.Library()


@register.filter(name='capitalize')
def capitalize(value):
    """
    Capitalizes the value, i.e. Makes the first letter capital
    and lowers the rest

    * THIS iS TExt => This is text
    """
    value = str(value)
    return value[0].upper() + value[1:].lower()
