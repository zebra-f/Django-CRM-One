from django.shortcuts import render
from django.http import HttpResponse

from .models import Product, Order, Customer
# Create your views here.


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    variables = {
        'orders': orders,
        'customers': customers
        }

    return render(request, 'accounts/dashboard.html', context=variables)


def products(request):
    products = Product.objects.all()
    variables = {
        'products': products
        }

    return render(request, 'accounts/products.html', context=variables)


def customers(request):
    customers = Customer.objects.all()
    variables = {
        'customers': customers
    }

    return render(request, 'accounts/customers.html', context=variables)