from django.db import models

# Create your models here.
class cart(models.Model):
   name=models.CharField(max_length=50)
   price = models.IntegerField()#    (max_digits=4,decimal_places=2)
   quantity=models.IntegerField() #(max_digits=4,decimal_places=2)
   total=models.IntegerField() #(max_digits=3,decimal_places=1)
   img_link=models.CharField(max_length=2083)
   user_id=models.IntegerField()
   product_id=models.IntegerField()