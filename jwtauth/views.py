from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse,HttpResponse
from rest_framework.views import APIView
from django.template.loader import render_to_string
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.response import Response
from jwtauth.customauthentication import CustomAuthentication
from jwtauth.logincheck import login_url_check
from jwtauth.form import EmailForm
from django.utils.decorators import method_decorator
import json
from django.core.mail import send_mail
from django.conf import settings
import pytz
from datetime import datetime



def usercreation(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('userlogin')
        
        return render(request,'registration.html',{'form':form})
    else:
        form=UserCreationForm()
        return render(request,'registration.html',{'form':form})
    

def userlogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        usr=authenticate(username=username,password=password)
        if usr is not None:            
            next_url=request.GET.get('next')
            refresh = RefreshToken.for_user(usr)
            if next_url:
                spl=next_url.split('/auth/')[-1]
                reverse_url=reverse(spl)
                response = HttpResponse(status=302)
                response['Location'] = reverse_url
            else:
                response=redirect('home')
            
            response.set_cookie('refresh_token', str(refresh), httponly=True)
            response.set_cookie('access_token', str(refresh.access_token), httponly=True)
            return response            
        
        return render(request,'login.html')
    else:
        try:
            token = request.COOKIES.get('refresh_token')
            if token is None:
                return render(request,'login.html')
            return redirect('home')
        except:
            return render(request,'login.html')

def userlogout(request):   
    response=redirect('userlogin')
    response.delete_cookie('refresh_token')  
    response.delete_cookie('access_token') 
    return response


@login_url_check
@api_view(['GET'])
@authentication_classes([CustomAuthentication])
def home(request):     
    return render(request,'home.html')

@method_decorator(login_url_check, name='dispatch')
class emailcreation(APIView):
    authentication_classes=[CustomAuthentication]
    def get(self,request):
        form=EmailForm()
        return render(request,'email.html',{'form':form})
    def post(self,request,*args,**kwargs):
        form=EmailForm(request.POST)
        if form.is_valid():
            email=form.save(commit=False)
            email.user=request.user
            email.save()
            return redirect('home')
        return render(request,'email.html',{'form':form})