from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('properties/', views.product_list_view, name='properties'),
    path('contact/', views.contact_view, name='contact'),
    path('house-detail/<int:house_id>/', views.house_detail_view, name='house-detail'),
]
