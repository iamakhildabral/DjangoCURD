from django.shortcuts import render
from rest_framework import viewsets
from .models import Company, Employee

# Create your views here.
from .serializers import CompanySerializers, EmployeeSerializers


# creating views for the company
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers


# creating views for the employee
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
