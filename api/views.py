from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Company, Employee

# Create your views here.
from .serializers import CompanySerializers, EmployeeSerializers


# creating views for the company
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers

    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):
        


# creating views for the employee
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
