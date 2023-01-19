from django.urls import path

from .import views

urlpatterns = [
    path('customer/register', views.createCustomer.as_view(), name='createCustomer'),
    path('customer/<str:phone>', views.customer_validation, name='validate_customer'),
]