from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customers/', views.customers, name='customers'),
    path('customer/<int:id>/', views.customer, name='customer'),

    path('create_order/', views.create_order, name='create_order')
]
