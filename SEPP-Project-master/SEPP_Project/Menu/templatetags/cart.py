from django import template
register = template.Library()

@register.filter(name='in_cart')
def in_cart(Product,cart):
    for p in cart:
        if int(p.product_id) == Product.id and p.quantity > 0 :
            # print((p.product_id))
            # print((Product.id))
            return True
    return False

@register.simple_tag(name='quantity')
def quantity(Product,*args,**kwargs):
    cart=kwargs['cart']
    print(cart)
    print(kwargs['cart'])
    # print("123")
    for p in cart:
        print(kwargs['uid'])
        print(p.user_id)
        if int(p.product_id) == Product.id and int(kwargs['uid']) == int(p.user_id) :
            print("hello")
            return p.quantity
    return 0


@register.filter(name="type")
def type(Product,t):
    if Product.type == t:
        return True
    return False

@register.filter(name="special")
def special(Product,sp):
    if Product.special == sp:
        return True
    return False

@register.filter(name="mb")
def mb(Product):
    if Product.timesOrdered>50:
        return True
    return False

@register.filter(name="uid")
def uid(cart,uid):
    
    for p in cart:
        if int(p.user_id) == uid:
            return True
    return False