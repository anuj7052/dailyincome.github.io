from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Expence(models.Model):
    expence=models.IntegerField()
    expence_type=models.CharField(max_length=30)
    expence_date=models.DateField()
    description=models.TextField(max_length=300)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table='expence'

from django import forms

class ExpenceForm(forms.ModelForm):
    class Meta:
        model=Expence
        fields='__all__'