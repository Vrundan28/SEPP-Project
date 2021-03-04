from django import template 
register = template.Library()


@register.filter(name='in_cart')  
def in_cart(product,cart):
   for p in cart:
      if p.id==product.id:
         return True
   return False