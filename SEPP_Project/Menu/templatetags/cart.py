from django import template
register = template.Library()

@register.filter(name='in_cart')
def in_cart(Product,cart):
    for p in cart:
        if int(p.product_id) == Product.id and p.quantity > 0 :
            return True
    return False

@register.filter(name='quantity')
def quantity(Product,cart):
    for p in cart:
        if int(p.product_id) == Product.id :
            return p.quantity
    return 0