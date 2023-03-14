from django.shortcuts import render
from dbdemo.models import employee 
# Create your views here.
def empdetail(request):

    emp_data = employee.objects.all()
    emp_dict = {'employee_list' : emp_data}
    return render (request,'temp/a.html',context = emp_dict )