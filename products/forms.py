from django import forms
from .models import *


class ProductForms(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.filter(status=True))
    size = forms.CharField(max_length=255, label="Cake size : (diameter x height in inches):")
    class Meta: 
        model = Products
        fields = ["product_name", "category", "price", "size", "status"]

       
   
