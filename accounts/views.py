from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Product, Order, Customer
from .forms import OrderForm, RegisterUserForm, LoginUserForm
from .filters import OrderFilter
from . import decorators

# Create your views here.

def home(request):

    return render(request, 'accounts/home.html')


# Dashboard
@login_required(login_url='login_user')
def dashboard(request):

    if request.method == "POST":
        order_id = request.POST['delete-order'].split('-')[-1]
        order = Order.objects.get(id=int(order_id))
        order.delete()

        return redirect('dashboard')
        

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


@login_required(login_url='login_user')
def products(request):
    products = Product.objects.all()
    
    context = {
        'products': products,
        }

    return render(request, 'accounts/products.html', context=context)


@login_required(login_url='login_user')
def customers(request):
    customers = Customer.objects.all()
    context = {
        'customers': customers,
    }

    return render(request, 'accounts/customers.html', context=context)


@login_required(login_url='login_user')
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
@login_required(login_url='login_user')
def create_order(request):
    
    form = OrderForm()
    
    if request.method == "POST":
        form = OrderForm(request.POST)

        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect('dashboard')

    context = {
        'form': form
    }   
    
    return render(request, 'accounts/order_form.html', context=context)


@login_required(login_url='login_user')
def create_order_p(request, id):
    ''' id: cusotomer id
    '''
    customer = Customer.objects.get(id=id)
    form = OrderForm(initial={
            'customer': customer,
        })
    
    if request.method == "POST":
        form = OrderForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect(f'/customer/{id}')
    
    context = {
        'form': form,
        'mutiple_forms': True, 
    }
    
    return render(request, 'accounts/order_form.html', context=context)


# ORDER_FORM.HTML
@login_required(login_url='login_user')
def update_order_p(request, id):
    ''' id: order id
    '''
    order = Order.objects.get(id=id)
    form = OrderForm(instance=order)

    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form
    }

    return render(request, 'accounts/order_form.html', context=context)


# REGISTER/LOGIN
@decorators.authenticated_user
def register_user(request):
    
    # # moved to decorators.authenticated_user
    # if request.user.is_authenticated:
    #     messages.info(request, "Log out first if you'd to register a new user") 
    #     return redirect('dashboard')

    form = RegisterUserForm
    
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account {username} was successfully createad.')

            return redirect('login_user')
    
    context = {
        'form': form,
    }

    return render(request, 'accounts/register_form.html', context=context)


@decorators.authenticated_user
def login_user(request):
    form = LoginUserForm

    if request.method == "POST":
        form = LoginUserForm(data=request.POST)
        
        if form.is_valid():
            form.clean()
            # username = request.POST['username']
            # password = request.POST['password']
            # user = authenticate(request, username=username, password=password)
            # login(request, user)

            login(request, form.user_cache)
            return redirect('dashboard')
            
        else:
            pass
            # print(form.errors)

    context = {
        'form': form
    }

    return render(request, 'accounts/login_form.html', context=context)


def logout_user(request):

    logout(request)

    return redirect('home')


def user(request):
    
    if request.user.is_authenticated:
        user_greeting = f"Hello {request.user.email}"
    
    else:
        user_greeting = "Hello whoever you are"

    context = {
        'user_greeting': user_greeting
    }

    return render(request, 'accounts/user.html', context=context)

