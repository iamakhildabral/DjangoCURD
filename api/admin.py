from django.contrib import admin
from .models import Company,Employee

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name','location','type','active')
    search_fields = ('name',)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name','email','company')
    search_fields = ('name','email',)

# Register your models here.
admin.site.register(Company,CompanyAdmin)
admin.site.register(Employee,EmployeeAdmin)

