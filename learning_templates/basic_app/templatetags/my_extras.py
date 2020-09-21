from django import template

register = template.Library()

def cutt(value, arg):
    """
    This cut's out all the 'arg' from the string
    """
    return value.replace(arg, '')

register.filter('cutt', cutt)
