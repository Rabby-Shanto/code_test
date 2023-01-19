from django.db import models
from UserSubscription.Customer.models import Customer
import uuid

# Create your models here.

class Payment(models.Model):
    user = models.ForeignKey(Customer,on_delete=models.CASCADE)
    sub_name = models.CharField(max_length=100)
    subscription_total = models.FloatField()
    status = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=200,null=True,blank=True)
    order_id = models.CharField(max_length=200,null=True,blank=True)
    phone_number = models.CharField(max_length=15,null=True,blank=True)

    def __str__(self):
        return self.transaction_id

