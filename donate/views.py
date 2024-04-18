from .models import Donation
from .serializers import DonationSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


class DonationView(APIView):
    # @method_decorator(csrf_exempt)
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        donations = Donation.objects.all()
        serializer = DonationSerializer(donations, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DonationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)