from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from .models import Product, Order, Customer
from .forms import OrderForm
from .filters import OrderFilter

# Create your views here.

# Dashboard
def dashboard(request):

    if request.method == "POST":
        order_id = request.POST['delete-order'].split('-')[-1]
        order = Order.objects.get(id=int(order_id))
        order.delete()

        return redirect('/')
        

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
    
    if request.method == "POST":
        order_id = request.POST['delete-order'].split('-')[-1]
        order = Order.objects.get(id=int(order_id))
        order.delete()
        
        return redirect(f'/customer/{id}')
    
    customer = Customer.objects.get(id=id)
    orders = customer.order_set.all()
    
    # if else not necessary
    if len(request.GET) > 0:
        filter = OrderFilter(request.GET, queryset=orders)
        # .qs QuerySet
        orders = filter.qs
    else:
        filter = OrderFilter()
    
    context = {
        'customer': customer,
        'orders_count': orders.count(),
        'orders': orders,
        'filter': filter,
    }

    return render(request, 'accounts/customer.html', context=context)


# ORDER_FORM.HTML
def create_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)

        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect('/')

    form = OrderForm()
    context = {
        'form': form
    }   
    
    return render(request, 'accounts/order_form.html', context=context)


def create_order_p(request, id):
    ''' id: cusotomer id
    '''
    if request.method == "POST":
        form = OrderForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect(f'/customer/{id}')
    
    customer = Customer.objects.get(id=id)
    form = OrderForm(initial={
            'customer': customer,
        }) 
    context = {
        'form': form,
        'mutiple_forms': True, 
    }
    
    return render(request, 'accounts/order_form.html', context=context)


# ORDER_FORM.HTML
def update_order_p(request, id):
    ''' id: order id
    '''
    order = Order.objects.get(id=id)

    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)

        if form.is_valid():
            form.save()
            return redirect('/')
    
    form = OrderForm(instance=order)
    context = {
        'form': form
    }

    return render(request, 'accounts/order_form.html', context=context)


def register_user(request):

    form = UserCreationForm

    context = {
        'form': form,
    }

    return render(request, 'accounts/register_form.html', context=context)


def login_user(request):

    

    context = {
        'form': 'placeholder'
    }

    return render(request, 'accounts/login_form.html', context=context)

