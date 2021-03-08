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
                c = cart.objects.get(id = alreadythere.id)
                c.delete()
            
        except cart.DoesNotExist :
            carts=cart(name=itemInCart.product_name,price=itemInCart.price,total=0,quantity=1,img_link=itemInCart.image_url,user_id=curr_user.id,product_id = selectedId)
            carts.save()
    
    products_cart = cart.objects.all()
    products = Product_details.objects.all()
    return render(request,'viewMenu.html',{'products':products,'products_cart':products_cart}) 


def cone(request):
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
                c = cart.objects.get(id = alreadythere.id)
                c.delete()
            
        except cart.DoesNotExist :
            carts=cart(name=itemInCart.product_name,price=itemInCart.price,total=0,quantity=1,img_link=itemInCart.image_url,user_id=curr_user.id,product_id = selectedId)
            carts.save()
    products_cart = cart.objects.all()
    products = Product_details.objects.filter(type = "cone")
    return render(request,'filter.html',{'products':products,'products_cart':products_cart})
    
    
def candy(request):
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
                c = cart.objects.get(id = alreadythere.id)
                c.delete()
            
        except cart.DoesNotExist :
            carts=cart(name=itemInCart.product_name,price=itemInCart.price,total=0,quantity=1,img_link=itemInCart.image_url,user_id=curr_user.id,product_id = selectedId)
            carts.save()
    products_cart = cart.objects.all()
    products = Product_details.objects.filter(type = "candy")
    return render(request,'filter.html',{'products':products,'products_cart':products_cart})

def family_pack(request):
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
                c = cart.objects.get(id = alreadythere.id)
                c.delete()
            
        except cart.DoesNotExist :
            carts=cart(name=itemInCart.product_name,price=itemInCart.price,total=0,quantity=1,img_link=itemInCart.image_url,user_id=curr_user.id,product_id = selectedId)
            carts.save()
    products_cart = cart.objects.all()
    products = Product_details.objects.filter(type = "familypack")
    return render(request,'filter.html',{'products':products,'products_cart':products_cart}) 


def chocolate_icecream(request):
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
                c = cart.objects.get(id = alreadythere.id)
                c.delete()
            
        except cart.DoesNotExist :
            carts=cart(name=itemInCart.product_name,price=itemInCart.price,total=0,quantity=1,img_link=itemInCart.image_url,user_id=curr_user.id,product_id = selectedId)
            carts.save()

    products_cart = cart.objects.all()
    products = Product_details.objects.filter(flavour = "Chocolate")
    return render(request,'filter.html',{'products':products,'products_cart':products_cart})   


def strawberry_icecream(request):
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
                c = cart.objects.get(id = alreadythere.id)
                c.delete()
            
        except cart.DoesNotExist :
            carts=cart(name=itemInCart.product_name,price=itemInCart.price,total=0,quantity=1,img_link=itemInCart.image_url,user_id=curr_user.id,product_id = selectedId)
            carts.save()
    products_cart = cart.objects.all()
    products = Product_details.objects.filter(flavour = "Strawberry")
    return render(request,'filter.html',{'products':products,'products_cart':products_cart})  


def butterscotch_icecream(request):
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
                c = cart.objects.get(id = alreadythere.id)
                c.delete()
            
        except cart.DoesNotExist :
            carts=cart(name=itemInCart.product_name,price=itemInCart.price,total=0,quantity=1,img_link=itemInCart.image_url,user_id=curr_user.id,product_id = selectedId)
            carts.save()
    products_cart = cart.objects.all()
    products = Product_details.objects.filter(flavour = "Butterscotch")
    return render(request,'filter.html',{'products':products,'products_cart':products_cart})   
     
def vanila_icecream(request):
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
                c = cart.objects.get(id = alreadythere.id)
                c.delete()
            
        except cart.DoesNotExist :
            carts=cart(name=itemInCart.product_name,price=itemInCart.price,total=0,quantity=1,img_link=itemInCart.image_url,user_id=curr_user.id,product_id = selectedId)
            carts.save()
    products_cart = cart.objects.all()
    products = Product_details.objects.filter(flavour = "Vanila")
    return render(request,'filter.html',{'products':products,'products_cart':products_cart})   
   
def menu(request):
    return render(request,'menu.html')

def search(request):
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
                c = cart.objects.get(id = alreadythere.id)
                c.delete()
            
        except cart.DoesNotExist :
            carts=cart(name=itemInCart.product_name,price=itemInCart.price,total=0,quantity=1,img_link=itemInCart.image_url,user_id=curr_user.id,product_id = selectedId)
            carts.save()
    products_cart = cart.objects.all()
    
    search = request.GET["search"]
    productName = Product_details.objects.filter(product_name__icontains = search)
    productType = Product_details.objects.filter(type__icontains = search)
    productFlavour = Product_details.objects.filter(flavour__icontains = search)
    products = productName.union(productType)
    products = products.union(productFlavour)

    return render(request,'filter.html',{'products':products,'products_cart':products_cart,'search':search})   
     
