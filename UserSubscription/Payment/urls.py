from django.urls import path
from .import views

urlpatterns = [
 path('payment/<str:phone>/<str:subscription_name>',views.initiate_payment,name='payment'),
 path('validate_payment/<str:tran_id>',views.payment_status,name='payment_status')    

]
