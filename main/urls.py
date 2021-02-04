from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('collection/',views.collection,name='collection'),
    path('product-details/<str:slug>/',views.productdetails,name='product-details'),
    path('order_details/',views.order_details, name="order_details"),
    path('checkout/',views.checkout,name='checkout'),
    path('userprofile/',views.userprofile,name='userprofile'),
]
