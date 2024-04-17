from rest_framework import serializers
from .models import CustomUser
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed




class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=250)
    first_name = serializers.CharField(max_length=250)
    last_name = serializers.CharField(max_length=250)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password']

    def validate(self, args):
        email = args.get('email', None)
        first_name = args.get('first_name', None)
        last_name = args.get('last_name', None)

        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': 'Email already exists'})
        

        return super().validate(args)
    

    def create(self, validated_data):

        user = CustomUser.objects.create_user(**validated_data)

            
        return {
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name     
        }



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