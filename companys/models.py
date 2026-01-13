from django.db import models

# Create your models here.


class Companys(models.Model):
    name = models.CharField(max_length=255) # Ime tvrtke
    vat_id = models.CharField(max_length=50, blank=True, null=True) # OIB tvrtke
    street = models.CharField(max_length=255) # Ulica
    city = models.CharField(max_length=100) # Grad
    country = models.CharField(max_length=100) # Država


    def __str__(self):
        return f"{self.name} ({self.vat_id})"