from django.contrib import admin

# Register your models here.

from dbdemo.models import employee

class employeeadmin (admin.ModelAdmin):
    emp_detaial = ['emp_no','emp_name','emp_salary','emp_adress']


admin.site.register(employee,employeeadmin)