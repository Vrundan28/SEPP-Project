from django.conf.urls import url
from cart.views import viewcart
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
   url('viewcart/',viewcart),
]