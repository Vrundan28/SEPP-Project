from django.shortcuts import render
from .models import cart
from django.contrib.auth.models import User
from django.db import models
from django.http import HttpResponseRedirect

# Create your views here.

def viewcart(request):
   curr_user=request.user
   added=cart.objects.filter(user_id=curr_user.id)
   if request.method == "POST":
      total_qty=total_price=0
      thisprice=0
      thisqty=0
      for items in added:
         items.quantity= request.POST.get(items.name)
         items.save()
         thisprice=(items.price)
         thisqty=(items.quantity)
         print(items.price)
         
         total_price+=int(thisprice)*int(thisqty)
         #total_price+=Convert.ToDouble(items.price)*Convert.ToDouble(items.quantity)
         total_qty+=int(items.quantity)
      # request.session['added'] = added
      # request.session['total_qty']=total_qty
      # request.session['total_price']=total_price
      # return HttpResponseRedirect("/order/vieworder/")#,{'added':added ,'total_qty':total_qty ,'total_price':total_price})
      return HttpResponseRedirect("/order/vieworder/")
      # ?added=add&total_qty=total_qt&total_price=total_pric")
   else:
      return render(request, 'viewcart.html',{'c':added})
   # curr_user=request.user
   # added=cart.objects.filter(user_id=curr_user.id)
   # total_in_cart = 0
   # for item in added :
   #    total_in_cart += item.price
      