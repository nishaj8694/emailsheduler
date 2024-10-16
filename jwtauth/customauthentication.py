from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed, NotAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken



class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.COOKIES.get('refresh_token')
        if not token:
            raise NotAuthenticated('Token is missing, redirect to login')    
        try:
            token_validation = RefreshToken(token)            
        except Exception as e:
            if 'Token is invalid or expired'==str(e):
                raise AuthenticationFailed('You are not authorized')
            raise AuthenticationFailed('Invalid access token')
        userID = token_validation['user_id'] 
        try:
            user = User.objects.get(id=userID)
        except User.DoesNotExist:
            raise AuthenticationFailed('User not found')
        return (user, None)