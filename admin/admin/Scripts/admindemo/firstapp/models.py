from django.db import models

# Create your models here.

class Emp(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    contact=models.CharField(max_length=30)

class account(models.Model):
    salary=models.IntegerField()
    month=models.CharField(max_length=30)

    emp=models.ForeignKey(Emp,on_delete=models.CASCADE)

