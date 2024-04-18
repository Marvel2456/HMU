from .models import Donation
from .serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated



class DonationView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        donations = Donation.objects.all().order_by('-timestamp')

        cash_donations = donations.filter(method='cash')
        pledge_donations = donations.filter(method='pledge')
        transfer_donations = donations.filter(method='transfer')
        
        cash_transfer_donations = sum(donation.amount for donation in cash_donations) + \
                                  sum(donation.amount for donation in transfer_donations)
        pledges_donations = sum(donation.amount for donation in pledge_donations)
        total_donations = sum(donation.amount for donation in donations)

        donations_serializer = DonationSerializer(donations, many=True)

        data = {
            'donations': donations_serializer.data,
            'total_donations': total_donations,
            'cash_transfer_donations': cash_transfer_donations,
            'pledges_donations': pledges_donations,
        }

        return Response(data)

    def post(self, request, format=None):
        serializer = DonationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, format=None):
        data = request.data
        donation_id = data.get('id')
        if not donation_id:
            return Response({'error': 'Donation ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            donation = Donation.objects.get(pk=donation_id)
        except Donation.DoesNotExist:
            return Response({'error': 'Donation not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = DonationUpdateSerializer(donation, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)