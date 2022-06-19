from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('products/', views.products, name='products'),
    path('customers/', views.customers, name='customers'),
    path('customer/<int:id>/', views.customer, name='customer'),
    path('user/', views.user, name='user'),

    # ORDER UPDATE/CREATE/DELETE
    path('create_order/', views.create_order, name='create_order'),
    path('create_order/<int:id>/', views.create_order_p, name='create_order_p'),
    path('update_order/<int:id>/', views.update_order_p, name='update_order_p'),

    # LOGIN/REGISTER
    path('register/', views.register_user, name='register_user'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
]
