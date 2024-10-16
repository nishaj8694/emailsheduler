from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)
from jwtauth import views

urlpatterns = [
     path('usercreation',views.usercreation,name='usercreation'),
     path('userlogin',views.userlogin,name='userlogin'),
     path('userlogout',views.userlogout,name='userlogout'),
     path('home',views.home,name='home'),
     path('emailcreation',views.emailcreation.as_view(),name='emailcreation'),
     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]