from django.urls import path
from .views import *

urlpatterns = [
    path('make_donation/', DonationView.as_view(), name='make-donation'),
    path('get_donation/', DonationView.as_view(), name='get-donation'),
    path('update_donations/', DonationView.as_view(), name='update-donation'),
]

