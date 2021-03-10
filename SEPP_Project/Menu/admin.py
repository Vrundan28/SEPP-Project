from django.contrib import admin
from .models import Product_details

class Product_DetailsAdmin(admin.ModelAdmin):
    list_display = (
        'product_name','price','type','flavour','Status','image_url','special','timesOrdered'
    )

admin.site.register(Product_details,Product_DetailsAdmin)    