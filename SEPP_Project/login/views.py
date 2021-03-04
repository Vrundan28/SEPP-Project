
# Create your views here.
# from SEPP_Project.login.models import User_Details
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from .models import User_Details


def log_in(request):
   if request.method == "POST":
      user = auth.authenticate(username=request.POST.get('username'),password=request.POST.get('password'))

      if user is not None:
         auth.login(request, user)
         return HttpResponseRedirect('/Menu/viewMenu/',{'uid':user.id})
      else:
         return HttpResponseRedirect('/login/invalidlogin/')
   else:  
      return render(request,'log_in.html')

def update(request):
    if request.method == "POST":
        user = auth.authenticate(username = request.user.username, password = request.POST.get('password'))
        updateUser = User_Details.objects.get(user_id = user.id)
        updateUser.phone_no = request.POST.get('phone_number')
        updateUser.address = request.POST.get('address')    
        user.email = request.POST.get('email')
        user.first_name = request.POST.get('fname')
        user.last_name = request.POST.get('lname')
        user.username = request.POST.get('username')
        user.save()
        updateUser.save()
        return HttpResponseRedirect('/Menu/viewMenu/')#,{'user_id':user})
        # return render(request,'Menu/viewMenu/',{'error' : "Updated Successfully"})
    else:
        curr_user = request.user
        current_user = User_Details.objects.get(user_id = curr_user.id)
        # products = User_Details.objects.all()
        # print(current_user.phone_no)
        return render(request,'update.html',{'details' : current_user})

def signup(request):
    if request.method == "POST":
      #   request.POST = request.POST
      if request.POST.get('username'):
         if request.POST.get('password'):    
            if request.POST.get('password') == request.POST.get('confirm_password'):
               try:
                  user = User.objects.get(username=request.POST.get('username'))
                  return render(request, 'signup.html', {'error': "Username Already Taken "})
                  #  return HttpResponse("User already exists")
               except User.DoesNotExist: 
                  user = User.objects.create_user(username=request.POST.get('username'), password=request.POST.get('password'),first_name=request.POST.get('fname'),last_name=request.POST.get('lname'), email=request.POST.get('email'))
                  newUser = User_Details()
                  newUser.setAttribute(request.POST.get('phone_number'),request.POST.get('address'),user.id)
                  newUser.save()
                  auth.login(request, user)
                  return HttpResponseRedirect('/Menu/viewMenu/')
            else:
               return render(request, 'signup.html', {'error': "Entered passwords do not match"})
            # return HttpResponse("Passwords do not match")
         else:
            return render(request, 'signup.html', {'error': "Please Enter Password"})
      else:
         return render(request, 'signup.html', {'error': "Please Enter Username"})
    else:
        return render(request, 'signup.html')

def loggedin(request):
   return render(request,'loggedin.html', {"full_name":request.user.username})

def invalidlogin(request):
   return render(request,'invalidlogin.html')

def logout(request):
   auth.logout(request)
   return render(request,'logout.html')