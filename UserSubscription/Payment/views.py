from sslcommerz_lib import SSLCOMMERZ
from .models import Payment
from UserSubscription.Customer.models import Customer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import PaymentSerializer
from UserSubscription.Company.models import Subscription




@api_view(['GET', 'POST'])
def initiate_payment(request,phone,subscription_name):

    # filtering the customer's who have no active subscriptions

    non_subCustomer = Customer.objects.filter(phone_number=phone,has_active_Subscription=False)
    subscription = Subscription.objects.filter(plan=subscription_name).values('cost')
    print(non_subCustomer)

    if non_subCustomer:

        try:
            subscription = Subscription.objects.get(plan=subscription_name).values('cost')
            print(subscription)
            subscription_total = subscription[0]['cost']
            # creating payment objects where phone_number will be provided in url
            order = Payment.objects.create(
                                    # subscription_total=subscription_price,\
                                    sub_name=subscription_name,\
                                    phone_number = phone,
                                    subscription_total=subscription_total)

            serializer = PaymentSerializer(order)
            if serializer.is_valid:
                serializer.save()
                                        
            # SSLCOMMERZ sandbox
            # need to create a sandbox account
            settings = { 'store_id': '****', 'store_pass': '****', 'issandbox': True }
            sslcz = SSLCOMMERZ(settings)
            post_body = {}
            post_body['cus_phone'] = phone

            post_body['product_name'] = subscription_name

            # creating SSLCOMMERZ session for payment
            response = sslcz.createSession(post_body) # API response


            return Response({'Response': response},serializer.data)

        except:

            return Response({'res':'Payment Unsuccessful!'})

    else:

        return Response({'Res': 'You already have active subscription'})
            


        
        







    



@api_view(['GET'])
def payment_status(request,tranid):

        # SSLcommerze sandbox account 
        settings = { 'store_id': 'testbox', 'store_pass': 'qwerty', 'issandbox': True }
        sslcz = SSLCOMMERZ(settings)

        # verifying through transaction id that will be given after purchasing subscriptions
        res = sslcz.transaction_query_tranid(tranid)

        return Response({"Status" : res})





