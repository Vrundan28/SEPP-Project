from django.db import models

# Create your models here.
class User_Details(models.Model):
    user_ID = models.AutoField(primary_key="user_id")
    name = models.CharField(max_length=25)
    phone_no = models.IntegerField()
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=2)
    
class Customer_Details(models.Model):
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=11)

class Admin_Details(models.Model):
    adminname = models.CharField(max_length=25)
    password = models.CharField(max_length=11)

class Employee_Details(models.Model):
    employeename = models.CharField(max_length=25)
    password = models.CharField(max_length=11)

class Product_details(models.Model):
    product_ID = models.AutoField(primary_key="product_id")
    product_name = models.CharField(max_length=25)
    flavour = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=4,decimal_places=2)
    type = models.CharField(max_length=20)
    Status = models.CharField(max_length=15 ,default="Available")

class Order(models.Model):
    order_ID = models.AutoField(primary_key="order_id")
    Order_details = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    bill = models.DecimalField(max_digits=4,decimal_places=2)
    deliveryStatus = models.CharField(max_length=50,default="Reviewing Your order")
    deliveryboysDetails = models.CharField(max_length=50)

class Payment(models.Model):
    BillAmount = models.DecimalField(max_digits=4,decimal_places=2)
    paymentMethod = models.CharField(max_length=20)