from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='Shopname'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='Contact Us'),
    path('tracker', views.tracker, name='tracker'),
    path('search', views.search, name='search'),
    path('productview', views.product, name='product view'),
    path('checkout', views.checkout, name='checkout'),

]