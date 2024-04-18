from rest_framework import serializers
from .models import Donation



class DonationSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(max_length=250,  allow_null=True)
    amount = serializers.IntegerField(default=0,  allow_null=True)
    method = serializers.CharField(max_length=100, allow_null=True)
    phone_number = serializers.CharField(max_length=100, allow_null=True)
    class Meta:
        model = Donation
        fields = ['full_name', 'amount', 'method', 'phone_number']