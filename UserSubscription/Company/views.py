from django.shortcuts import render
from .models import Company
from rest_framework.generics import ListCreateAPIView
from .serializer import CompanySerializer
from rest_framework.decorators import api_view

# Create your views here.

class CompanyView(ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


