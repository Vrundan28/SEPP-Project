from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Product_details
from cart.models import cart
from django.contrib.auth.models import User

# Create your views here.
def viewMenu(request):
     # print(products)
    if request.method =="POST":       
        # print(Product_details.product_name) 
        selectedId=request.POST.get('id')
        itemInCart=Product_details.objects.get(id=selectedId)
        try:
            # print("Jainil")
            curr_user = request.user
            alreadythere = cart.objects.get(name=itemInCart.product_name, user_id=curr_user.id)
            #print(alreadythere.quantity)
            # for item in alreadythere:

            alreadythere.quantity=alreadythere.quantity+1
            alreadythere.save()
            # print(alreadythere.quantity)
        except cart.DoesNotExist :
            carts=cart(name=itemInCart.product_name,price=itemInCart.price,quantity=1,total=0,img_link=itemInCart.image_url,user_id=curr_user.id,product_id=selectedId)
            carts.save()
    p_c=cart.objects.all()
    products = Product_details.objects.all()
    
    return render(request,'viewMenu.html',{'products':products,'cart':p_c})


def cone(request):
    products = Product_details.objects.filter(type = "cone")
    return render(request,'filter.html',{'products':products})
    
    
def candy(request):
    products = Product_details.objects.filter(type = "candy")
    return render(request,'filter.html',{'products':products})   


def family_pack(request):
    products = Product_details.objects.filter(type = "family pack")
    return render(request,'filter.html',{'products':products})   


def chocolate_icecream(request):
    products = Product_details.objects.filter(flavour = "Chocolate")
    return render(request,'filter.html',{'products':products})   


def strawberry_icecream(request):
    products = Product_details.objects.filter(flavour = "Strawberry")
    return render(request,'filter.html',{'products':products})   


def butterscotch_icecream(request):
    products = Product_details.objects.filter(flavour = "Butterscotch")
    return render(request,'filter.html',{'products':products})   
     
def vanila_icecream(request):
    products = Product_details.objects.filter(flavour = "vanila")
    return render(request,'filter.html',{'products':products})   
   

def search(request):
    
    search = request.GET["search"]
    productName = Product_details.objects.filter(product_name__icontains = search)
    productType = Product_details.objects.filter(type__icontains = search)
    productFlavour = Product_details.objects.filter(flavour__icontains = search)
    products = productName.union(productType)
    products = products.union(productFlavour)

    return render(request,'search.html',{'products':products,'search':search})   
