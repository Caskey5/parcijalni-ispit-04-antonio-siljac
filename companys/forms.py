from django import forms
from .models import Companys

class CompanysForm(forms.ModelForm):
    class Meta:
        model = Companys
        fields = ['name', 'vat_id', 'street', 'city', 'country']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'vat_id': forms.TextInput(attrs={'class': 'form-control'}),
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
        }