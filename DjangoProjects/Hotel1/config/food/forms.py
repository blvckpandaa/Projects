from django import forms
from .models import *


class OrderForm(forms.ModelForm):
    address=forms.CharField(widget=forms.TextInput(attrs={'class':'input', 'style':'border-radius:20px; background:none; border'}), label='Write your address')
    phone=forms.CharField(widget=forms.TextInput(attrs={'class':'input', 'style':'border-radius:20px;'}), label='Write your phone number')

    class Meta:
        model=Order
        fields=['address', 'phone']

