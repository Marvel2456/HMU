from rest_framework import serializers
from .models import CustomUser
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed






class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=250, min_length=6)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    tokens = serializers.CharField(read_only=True)
    
    
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'tokens']
        
    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        
        user = auth.authenticate(email=email, password=password)
        
        if not user:
          raise AuthenticationFailed('Invalid credentials, try agian') 
        if not user.is_active:
            raise AuthenticationFailed('Your account has been disabled, contact Admin')
        
        return {
            'email': user.email,
            'tokens' : user.tokens,    
        }