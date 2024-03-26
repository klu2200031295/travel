from django.db import models
from .forms import *
class Register (models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=100)
    phonenumber = models.PositiveBigIntegerField()
    class Meta:
        db_table="Register"


class PieChartForm(forms.Form):
    y_values = forms.CharField(label='Y Values', help_text='Enter comma-separated values')
    labels = forms.CharField(label='Labels', help_text='Enter comma-separated labels')

class ContactUs(models.Model):
    firstname=models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email=models.EmailField(primary_key=True)
    comment=models.TextField(max_length=300)
    class Meta:
        db_table="contactus"





# Create your models here.
