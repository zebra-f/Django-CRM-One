from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages


def authenticated_user(view_func):

    def wrapper_func(request, *args, **kwargs):
        
        if request.user.is_authenticated:
            if request.path == '/register/':
                messages.info(request, "Log out first if you'd to register a new user") 
                return redirect('dashboard')

            else:
                return redirect('dashboard')
        
        else:
            return view_func

    return wrapper_func

