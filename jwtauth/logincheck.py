from rest_framework.exceptions import AuthenticationFailed, NotAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken
from rest_framework_simplejwt.exceptions import InvalidToken,TokenError
# from .models import customUser
# from .customException import TokenException
from django.utils.http import urlencode
from django.shortcuts import render,redirect
from django.urls import reverse

def login_url_check(view_funct):
    def wrapper(request,*args,**kwargs):
        try:
            token = request.COOKIES.get('refresh_token')
            if not token:
                raise NotAuthenticated('Token is missing, redirect to login')  
        except(InvalidToken,TokenError,NotAuthenticated):    
            next_url = urlencode({'next': request.path})
            login_url = f"{reverse('userlogin')}?{next_url}"
            return redirect(login_url)
        
        return view_funct(request,*args,**kwargs)
    
    return wrapper