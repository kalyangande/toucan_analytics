from django.db import models
from django.contrib.auth.models import Permission


class CustomerData(models.Model):
    
    customer_Id  = models.IntegerField()
    category = models.CharField(max_length=20)
    mode_of_payments = models.CharField(max_length=25)
    amount_spent = models.FloatField()
    date = models.DateField()

class EMIData(models.Model):
    customer_Id  = models.IntegerField()
    EMI_paid_on_time = models.CharField(max_length=6)