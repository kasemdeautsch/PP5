from django import template

register = template.Library()


# Custom filter
@register.filter(name='calc_subtotal')
def calc_subtotal(quantitiy, price):
    return quantitiy * price
