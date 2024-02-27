from django import forms
from .models import Vehicle,Product,Vendor

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['vehicle_number', 'vehicle_type', 'dc_number', 'po_number', 'product']

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['name']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','vendor']
