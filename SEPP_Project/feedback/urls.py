from django.conf.urls import url
from .views import feedback


urlpatterns = [
    url('feedback/',feedback),
]