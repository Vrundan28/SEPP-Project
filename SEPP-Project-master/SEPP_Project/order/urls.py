from django.conf.urls import url
from .models import order_details
from .views import vieworder, payment, Credit_card, Paytm, success


urlpatterns = [
   url('vieworder/',vieworder),
   url('payment/',payment),
   url('Credit_card/',Credit_card),
   url('Paytm/',Paytm),
   url('success/',success),
]