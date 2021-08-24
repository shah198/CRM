from django import forms
from .models import *

class CustomerRegistration(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'email']
        widgets = {
            'name': forms.TextInput(),
            'phone': forms.TextInput(),
            'email': forms.TextInput(),
        }
