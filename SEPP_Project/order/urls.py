from django.conf.urls import url
from .models import order_details
from .views import vieworder 

urlpatterns = [
   url('vieworder/',vieworder),
   
]