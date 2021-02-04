from django.shortcuts import render
from .models import Products,CartDetails,Customer
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from .forms import UserData
import uuid,random

import datetime
from time import strftime

# Create your views here.
def index(request):
   login_user = request.user
   products=Products.objects.all()
   # custId = Customer.objects.get(user_id=login_user)
   # item_count = CartDetails.objects.filter(id_customer=custId).count()
   if 'add_item' in request.POST:
      prod_id = request.POST['getitemId']
      db_products = Products.objects.get(id=prod_id)
      added_time = strftime("%Y-%m-%d %H:%M:%S")
      # save_to_cart = CartDetails(id_product=db_products,date_cart=added_time,id_customer=custId).save()

   return render(request,'home.html',{'products':products}) 

def productdetails(request,slug):
   sl=Products.objects.get(slug=slug)
   
   return render(request,'product-details.html',{'sl':sl})

def order_details(request):
   custId = Customer.objects.get(user_id=request.user)
   cart_db = CartDetails.objects.filter(id_customer=custId)
   print(cart_db)

   return render(request,'order_details.html',{'cart_db':cart_db})

def checkout(request):
   return render(request,'checkout.html')

def collection(request):
   return render(request,'collection.html')

def userprofile(request):
   user_ = str(request.user.username)
   form_ = UserData() #instance to be added here
   print(user_)

   return render(request,'userprofile.html',{'form_':form_})