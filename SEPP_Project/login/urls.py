from .views import log_in, logout, signup, update, forgot_password
# from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
   url('signup/',signup),
   url('log_in/', log_in),
   url('logout/', logout),
   url('update/', update),
   url('forgot_password/',forgot_password),
   url('',log_in),
]
