from django.contrib import admin
from .models import cart

class cartAdmin(admin.ModelAdmin):
   list_display=('name','price','quantity','total','user_id')

admin.site.register(cart,cartAdmin)    