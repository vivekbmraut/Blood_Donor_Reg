from django.db import models
from django.db.models.deletion import CASCADE
# Create your models here.

class Doctor(models.Model):
    doc_id=models.BigAutoField(primary_key=True)
    doc_name=models.CharField(max_length=50)
    contact_no=models.BigIntegerField()
    doc_hospital=models.CharField(max_length=40)

class Donor(models.Model):
    donor_id=models.BigAutoField(primary_key=True)
    doctor_id=models.ForeignKey(Doctor,on_delete=models.CASCADE,to_field="doc_id")
    donor_name=models.CharField(max_length=40)
    blood_group=models.CharField(max_length=3)
    contact_no=models.BigIntegerField()
    last_donation=models.DateField()
    location_donation=models.CharField(max_length=40)