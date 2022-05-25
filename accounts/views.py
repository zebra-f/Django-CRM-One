from django.shortcuts import render
from django.http import HttpResponse

from .models import Product, Order, Customer
# Create your views here.


# Dashboard
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    context = {
        'orders': orders,
        'orders_count': orders.count(),
        'orders_count_pending': orders.filter(status='Pending').count(),
        'orders_count_delivered': orders.filter(status='Delivered').count(),
        'customers': customers,
        }

    return render(request, 'accounts/dashboard.html', context=context)


def products(request):
    products = Product.objects.all()
    context = {
        'products': products,
        }

    return render(request, 'accounts/products.html', context=context)


def customers(request):
    customers = Customer.objects.all()
    context = {
        'customers': customers,
    }

    return render(request, 'accounts/customers.html', context=context)


def customer(request, id):
    customer = Customer.objects.get(id=id)
    orders = customer.order_set.all()

    context = {
        'customer': customer,
        'orders_count': orders.count(),
        'orders': orders,
    }

    return render(request, 'accounts/customer.html', context=context)


# ORDER_FORM.HTML
def create_order(request):
    context = {
        
    }
    return render(request, 'accounts/order_form.html', context=context)