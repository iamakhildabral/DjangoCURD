from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Company, Employee
from rest_framework.response import Response

# Create your views here.
from .serializers import CompanySerializers, EmployeeSerializers


# creating views for the company
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers

    # companies/{companyId}/employees
    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        # First  getting the company id for which we'll be showing the records
        company = Company.objects.get(pk=pk)
        # now moving to the employees which matches with the company id in the employeed record
        employee = Employee.objects.filter(company=company)
        emp_serializer = EmployeeSerializers(employee,many=True,context={'request':request})
        return Response(emp_serializer.data)


# creating views for the employee
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
