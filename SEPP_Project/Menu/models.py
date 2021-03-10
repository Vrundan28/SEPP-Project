from django.db import models

class Product_details(models.Model):
    product_name = models.CharField(max_length=25)
    flavour = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=4,decimal_places=2)
    type = models.CharField(max_length=20)
    Status = models.CharField(max_length=15 ,default="Available")
    image_url = models.CharField(max_length=2083)
    special=models.IntegerField()
    timesOrdered=models.IntegerField()
    