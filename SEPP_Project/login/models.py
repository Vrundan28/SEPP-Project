from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User_Details(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=10)
    address = models.CharField(max_length=100)

    def setAttribute(self,phone_no,address,user_id):
        self.phone_no=phone_no
        self.address=address
        self.user_id=user_id
