from Menu.templatetags.cart import quantity
from django.shortcuts import render
from .models import Product_details
from cart.models import cart
from django.contrib.auth.models import User


def viewMenu(request):
    if request.method =="POST":       
        selectedId=request.POST.get('id')
        itemInCart=Product_details.objects.get(id=selectedId)
        try:
            curr_user = request.user
            alreadythere = cart.objects.get(name=itemInCart.product_name, user_id=curr_user.id)
            qty = int(request.POST.get('quantity'))
            if qty > 0:
                alreadythere.quantity = qty
                alreadythere.save()
            else:
                print("1234")
                c = cart.objects.get(id = alreadythere.id)
                c.delete()
            print("Jainil")
            
        except cart.DoesNotExist :
            print("vrundan")
            carts=cart(name=itemInCart.product_name,price=itemInCart.price,total=0,quantity=1,img_link=itemInCart.image_url,user_id=curr_user.id,product_id = selectedId)
            carts.save()
    
    products_cart = cart.objects.all()
    products = Product_details.objects.all()
    return render(request,'viewMenu.html',{'products':products,'products_cart':products_cart}) 


def cone(request):
    products = Product_details.objects.filter(type = "cone")
    return render(request,'filter.html',{'products':products})
    
    
def candy(request):
    products = Product_details.objects.filter(type = "candy")
    return render(request,'filter.html',{'products':products})   


def family_pack(request):
    products = Product_details.objects.filter(type = "familypack")
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
    products = Product_details.objects.filter(flavour = "Vanila")
    return render(request,'filter.html',{'products':products})   
   

def search(request):
    
    search = request.GET["search"]
    productName = Product_details.objects.filter(product_name__icontains = search)
    productType = Product_details.objects.filter(type__icontains = search)
    productFlavour = Product_details.objects.filter(flavour__icontains = search)
    products = productName.union(productType)
    products = products.union(productFlavour)

    return render(request,'search.html',{'products':products,'search':search})   
