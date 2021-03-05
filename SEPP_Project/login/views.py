from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from .models import User_Details


def home(request):
   return render(request,'home.html')

def forgot_password(request):
   if request.method == "POST":
      username = request.POST.get('username')
      users = User.objects.all()
      for user in users:
         if user.username == username:
            user1 = user
            break
      user1.set_password(request.POST.get('password'))
      user1.save()
      
      return HttpResponseRedirect('/login/log_in/',{'error':"Password updated successfully"})
   else:
      return render(request,'forgot_password.html')



def log_in(request):
   if request.method == "POST":
      user = auth.authenticate(username=request.POST.get('username'),password=request.POST.get('password'))

      if user is not None:
         auth.login(request, user)
         return HttpResponseRedirect('/Menu/viewMenu/')
      else:
         return render(request,'log_in.html',{'error':"Invalid Username or password"})
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
        return HttpResponseRedirect('/Menu/viewMenu/')
    else:
        curr_user = request.user
        current_user = User_Details.objects.get(user_id = curr_user.id)
        return render(request,'update.html',{'details' : current_user})


def signup(request):
    if request.method == "POST": 
      if request.POST.get('password') == request.POST.get('confirm_password'):
         try:
            user = User.objects.get(username=request.POST.get('username'))
            return render(request, 'signup.html', {'error': "Username Already Taken "})
            
         except User.DoesNotExist: 
            user = User.objects.create_user(username=request.POST.get('username'), password=request.POST.get('password'),first_name=request.POST.get('fname'),last_name=request.POST.get('lname'), email=request.POST.get('email'))
            newUser = User_Details()
            newUser.setAttribute(request.POST.get('phone_number'),request.POST.get('address'),user.id)
            newUser.save()
            auth.login(request, user)
            return HttpResponseRedirect('/Menu/viewMenu/')
      else:
         return render(request, 'signup.html', {'error': "Entered passwords do not match"})
    else:
        return render(request, 'signup.html')


def logout(request):
   auth.logout(request)
   return render(request,'log_in.html',{'error':"Logged out Successfully"})