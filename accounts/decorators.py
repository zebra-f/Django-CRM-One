from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages


def authenticated_user(view_func):

    def wrapper_function(request, *args, **kwargs):
        
        if request.user.is_authenticated:
            if request.path == '/register/':
                messages.info(request, "Log out first if you'd to register a new user") 
                return redirect('dashboard')

            else:
                return redirect('dashboard')
        
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_function


def allowed_users(allowed_roles = []):
    
    def decorator_function(view_func):

        def wrapper_function(request, *args, **kwargs):
            
            group = None
            
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("Not allowed to view this page")
        
        return wrapper_function

    return decorator_function



