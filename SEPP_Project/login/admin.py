from django.contrib import admin
from .models import User_Details

class User_DetailsAdmin(admin.ModelAdmin):
    list_display = ('id','address','phone_no')

admin.site.register(User_Details,User_DetailsAdmin)