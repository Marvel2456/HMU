from rest_framework import serializers
from .models import Donation



class DonationSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(max_length=250, allow_null=True, required=False)
    amount = serializers.IntegerField(default=0, allow_null=True, required=False)
    method = serializers.CharField(max_length=100, allow_null=True, required=False)
    phone_number = serializers.CharField(max_length=100, allow_null=True, required=False)
    is_announced = serializers.BooleanField(default=False, allow_null=True, required=False)
    as_anonymous = serializers.BooleanField(default=False, allow_null=True, required=False)

    class Meta:
        model = Donation
        fields = ['full_name', 'amount', 'method', 'phone_number', 'is_announced', 'as_anonymous']

class DonationUpdateSerializer(serializers.ModelSerializer):
    is_announced = serializers.BooleanField(required=False)

    class Meta:
        model = Donation
        fields = ['is_announced']