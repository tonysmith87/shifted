from django import template

register = template.Library()


@register.filter(name='keys')
def keys(value):
    return value.keys()


@register.filter(name='getvalue')
def getvalue(value, args):
    return value[args]
