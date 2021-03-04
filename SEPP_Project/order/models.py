from django.db import models

# Create your models here.

class order_details(models.Model):
   total_qty=models.IntegerField()
   # name=models.CharField(max_length=63)
   total_price=models.DecimalField(max_digits=6,decimal_places=2)
   u_id=models.IntegerField()
   

   