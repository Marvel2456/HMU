from django.db import models
import uuid

# Create your models here.


class Donation(models.Model):
    PAYMENT_METHOD = [
        ('cash', 'Cash'),
        ('transfer', 'Transfer'),
        ('pledge', 'Pledge'),
       
    ]
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    full_name = models.CharField(max_length=250, blank=True, null=True)
    amount = models.PositiveBigIntegerField(default=0, blank=True, null=True)
    method = models.CharField(max_length=50, choices=PAYMENT_METHOD, blank=True, null=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    is_announced = models.BooleanField(default=False, blank=True, null=True)
    as_anonymous = models.BooleanField(default=False, blank=True, null=True)


    def __str__(self):
        return f"{self.full_name} --- {self.amount} --- {self.timestamp} --- {self.is_announced }"