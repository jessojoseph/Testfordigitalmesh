from django.db import models

class Package(models.Model):
    name = models.CharField(max_length=100)
    rate = models.DecimalField(max_digits=10, decimal_places=2) 
    date_from = models.DateField()
    date_to = models.DateField()
    contact_no = models.CharField(max_length=15)

class Place(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE) 
    name = models.CharField(max_length=100)