from rest_framework import serializers
from .models import Company, Employee


# creating serializers
class CompanySerializers(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField()
    class Meta:
        model= Company
        fields= "__all__"

# creating employee serializer
class EmployeeSerializers(serializers.HyperlinkedModelSerializer):
    id= serializers.ReadOnlyField
    class Meta:
        model = Employee
        fields = "__all__"