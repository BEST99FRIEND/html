from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('product/', views.product_view, name='products'),
    path('contact/', views.contact_view, name='contact'),
]
