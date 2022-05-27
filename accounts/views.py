from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Product, Order, Customer
from .forms import OrderForm

# Create your views here.

# Dashboard
def dashboard(request):
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
    form = OrderForm()

    if request.method == "POST":
        form = OrderForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form
    }   
    
    return render(request, 'accounts/order_form.html', context=context)


# ORDER_FORM.HTML
def update_order(request, id):
    order = Order.objects.get(id=id)
    form = OrderForm(instance=order)
    
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)

        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form
    }

    return render(request, 'accounts/order_form.html', context=context)