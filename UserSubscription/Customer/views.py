from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Customer
from UserSubscription.Company.models import Company
from .serializer import CustomerSerializer
from rest_framework.generics import ListCreateAPIView
# Create your views here.


# creating and listing all customers

class createCustomer(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    


@api_view(['GET'])   

def customer_validation(request,phone):

        company_phone = []

        company_number = list(Company.objects.values('phone_number'))
        company_phone.append(company_number)

        customer = Customer.objects.filter(phone_number=phone)
        get_val = [obj['has_active_Subscription'] for obj in customer.values('has_active_Subscription') ]


        if get_val == [False]:

            # if phone_number doesn't got any sunscription,company get the phone_number
            company_phone.append({'phone_number': phone})

            res = f"Customer doesn't have any active Subscription,The number belongs to Company {','.join([obj['company_name__company_name'] for obj in customer.values('company_name__company_name') ])}"

        else:

            res = f"Customer has active subscription {','.join([obj['subscriptions__plan'] for obj in customer.values('subscriptions__plan') ])} and cost {customer.values('subscriptions__cost')}/month"

        return Response({"Caution!" : res})
            



