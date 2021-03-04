from django.urls import path
from .views import log_in, logout,loggedin, invalidlogin, signup, update
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
   url('signup/',signup),
   url('log_in/', log_in),
   url('logout/', logout),
   url('loggedin/', loggedin),
   url('invalidlogin/', invalidlogin),
   url('update/', update),
]
