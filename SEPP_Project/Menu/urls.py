from django.urls import path
from .views import butterscotch_icecream, chocolate_icecream, search, strawberry_icecream, viewMenu,cone,candy,family_pack,vanila_icecream,menu
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
    url('viewMenu/',viewMenu),
    url('cone/',cone),
    url('candy/',candy),
    url('family_pack/',family_pack),
    url('chocolate_icecream/',chocolate_icecream),
    url('strawberry_icecream/',strawberry_icecream),
    url('butterscotch_icecream/',butterscotch_icecream),
    url('vanila_icecream/',vanila_icecream),
    url('search/',search),
    url('menu/',menu),
]
