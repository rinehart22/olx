from django.contrib import admin
from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('read/<str:id>/', views.read_item, name='read'),
    path('update/<str:id>/', views.update, name='update'),
    path('delete/<str:id>/', views.delete, name='delete'),
    
    path('create/', views.create, name='create'),
    
    # path('search/', views.search_item, name='search'),

       path('s/', views.search_it, name='s'),

    path('phone/', views.product, name='phone'),
    
    path('allproducts/', views.all_products, name='all_products'),

    path('category/', views.categoryy, name='category'),



]
