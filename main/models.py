from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=50, null=True)
    number = models.CharField(max_length=50, null=True)

class Products(models.Model):
    name = models.CharField(max_length=100,null=True, blank=True)
    img = models.ImageField(upload_to='static/images')
    price = models.FloatField()
    delprice= models.FloatField()
    category=models.CharField(max_length=100,null=True, blank=True)
    brand=models.CharField(max_length=100,null=True, blank=True)
    color=models.CharField(max_length=100,null=True, blank=True)
    slug=models.SlugField(max_length=200,unique=True,null=True, blank=True)

    def __str__(self):
        return self.name    

class CartDetails(models.Model):   
    id_cart = models.AutoField(primary_key=True)
    id_product = models.ForeignKey(Products,on_delete=models.CASCADE, null=True, blank=True)
    id_customer = models.ForeignKey(Customer,on_delete=models.CASCADE, null=True, blank=True)
    date_cart = models.DateTimeField(auto_now=True, null=True, blank=True)

    def int(self):
        return self.id_cart

class OrderDetails(models.Model):
    id_order = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Products,on_delete=models.CASCADE)
    customer_id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    cart_id = models.ForeignKey(CartDetails,on_delete=models.CASCADE)
    total_items = models.CharField(max_length=120,null=True, blank=True)
    total_price = models.CharField(max_length=60,null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now=True)

    
class ShippingDetails(models.Model):
    id_shipping = models.AutoField(primary_key=True)
    id_order_id = models.ForeignKey(OrderDetails,on_delete=models.CASCADE)
    phone_no = models.IntegerField(null=True, blank=True)
    door_no = models.CharField(max_length=120,null=True, blank=True)
    address = models.CharField(max_length=220,null=True, blank=True)
    city = models.CharField(max_length=220,null=True, blank=True)
    pincode = models.CharField(max_length=120,null=True, blank=True)



    

