from django.shortcuts import render
from rest_framework import viewsets
from .models import Company

# Create your views here.
from .serializers import CompanySerializers


# creating views
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers
