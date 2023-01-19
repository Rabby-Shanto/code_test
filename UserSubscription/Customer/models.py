from django.db import models
import random
from UserSubscription.Company.models import Subscription,Company
from django.contrib.auth.models import User

# Create your models here.





class Customer(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=50)
    company_name = models.ForeignKey(Company,on_delete=models.CASCADE)
    email = models.EmailField(max_length=50,null=True,blank=True)
    phone_number = models.AutoField(primary_key=True,unique=True)
    subscriptions = models.ForeignKey(Subscription,on_delete=models.CASCADE,null=True,blank=True)
    has_active_Subscription = models.BooleanField(default=False)

    # method to generate random phone number
    def save(self, *args, **kwargs):
        while not self.pk:
            self.phone_number = '+8801'+ str(random.randint(100000000,999999999))
            try:
                Customer.objects.get(phone_number=self.phone_number)
            except Customer.DoesNotExist:
                break
        super(Customer, self).save(*args, **kwargs)

    def __str__(self):

        return f'{self.customer_name}-->[{self.phone_number}]'


    def total_cost(self):
        
        if self.subscriptions.plan:
            cost = self.subscription.cost

        return cost





