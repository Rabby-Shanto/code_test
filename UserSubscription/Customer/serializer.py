from rest_framework import serializers
from .models import Customer

'''
Use Just to show the foreign key values to response
company_name = serializers.CharField(source='company_name.company_name',allow_null=True)
subscriptions = serializers.CharField(source='subscriptions.plan',allow_null=True)

'''
class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = "__all__"