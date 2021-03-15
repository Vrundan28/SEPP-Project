from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import cart
from Menu.models import Product_details
from django.urls import reverse


# Create your views here.

def viewcart(request):
   curr_user=request.user
   added=cart.objects.filter(user_id=curr_user.id)
   
   if request.method == "POST":

      if 'place_order' in request.POST:
         return HttpResponseRedirect('/order/vieworder/')
      else:
         selectedId=request.POST.get('id')
         # itemInCart=Product_details.objects.get(id=selectedId)
         print(selectedId)
         curr_user = request.user
         alreadythere = cart.objects.get(product_id=selectedId, user_id=curr_user.id)
         print(alreadythere.product_id)
         qty = int(request.POST.get('quantity'))
         # print(qty)
         if qty > 0:
            alreadythere.quantity = qty
            alreadythere.save()
         else:
            c = cart.objects.get(id = alreadythere.id)
            c.delete()
         
   
   return render(request, 'viewcart.html',{'c':added})
      