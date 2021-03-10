from django.shortcuts import render
from cart.models import cart
from .models import order_details
from cart.models import cart
from Menu.models import Product_details
from django.contrib.auth.models import User
# Create your views here.

def vieworder(request):
   if request.method=="POST":
      return render (request,"payment.html")
   else:
      curr_user=request.user
      added=cart.objects.filter(user_id=curr_user.id)

      totalqty=totalprice=0
 
      for items in added:
         totalprice+=int(items.price)*int(items.quantity)
         totalqty+=int(items.quantity)
      
      order=order_details(total_price=totalprice,total_qty=totalqty,u_id=curr_user.id)   

      return render(request,'vieworder.html',{'o':order,'added':added})

def Paytm(request):
   return render(request,'Paytm.html')

def Credit_card(request):
   return render(request,'Credit_card.html')

def payment(request):
   return render(request,'payment.html')

def success(request):

   # Product_details.timesOrdered=Product_details.timesOrdered+1
   curr_user = request.user
   c = cart.objects.filter(user_id = curr_user.id)
   for p in c:
      pid=Product_details.objects.get(id=p.product_id)
      
      pid.timesOrdered = pid.timesOrdered+1
      
      pid.save()
      p.delete()
   return render(request,'success.html')