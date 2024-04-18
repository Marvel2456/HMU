from django.urls import path
# from django.views.decorators.csrf import csrf_exempt
from .views import *

urlpatterns = [
    path('make_donation/', DonationView.as_view(), name='make-donation'),
    path('get_donation/', DonationView.as_view(), name='get-donation'),
]
