from django import template

register = template.Library()

@register.filter
def seats_left(event):
    return event.seats_left()

@register.filter
def div(value, arg):
    try:
        return (float(value) / float(arg)) * 100
    except (ValueError, ZeroDivisionError, TypeError):
        return 0