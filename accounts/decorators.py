from django.http import HttpResponse
from django.shortcuts import redirect


def authenticated_user(view_func):

    def wrapper_func(request, *args, **kwargs):
        
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func

    return wrapper_func

