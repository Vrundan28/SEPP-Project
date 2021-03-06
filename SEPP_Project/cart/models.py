from django.db import models

# Create your models here.
class cart(models.Model):
   name=models.CharField(max_length=50)
   price = models.IntegerField()
   quantity=models.IntegerField()
   total=models.IntegerField() 
   img_link=models.CharField(max_length=2083)
   user_id=models.IntegerField()
   product_id=models.IntegerField()