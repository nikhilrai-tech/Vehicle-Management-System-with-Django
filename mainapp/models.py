from django.db import models
from django.contrib.auth.models import User

class Vendor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) :
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)

    def __str__(self) :
        return self.name

class Vehicle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle_number = models.CharField(max_length=20)
    vehicle_type = models.CharField(max_length=50)
    dc_number = models.CharField(max_length=50)
    po_number = models.CharField(max_length=50)
    quality_check = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.vehicle_number} - {self.vehicle_type} - {self.dc_number} - {self.po_number} - {self.quality_check}"
    
    def delete(self, *args, **kwargs):
        if self.product:
            self.product.delete()
            vendor = self.product.vendor
            if not vendor.product_set.exclude(id=self.product.id).exists():
                vendor.delete()
        super().delete(*args, **kwargs)