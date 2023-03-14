from django.db import models

# Create your models here.

class employee (models.Model):
    emp_no = models.IntegerField()
    emp_name = models.CharField(max_length = 50)
    emp_salary = models.FloatField(max_length = 50 )
    emp_adress = models.CharField(max_length = 150)