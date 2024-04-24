from django import forms
from .models import properyListdetails, property

class PropertyListDetailForm(forms.ModelForm):
    class Meta:
        model = property
        fields = '__all__'
