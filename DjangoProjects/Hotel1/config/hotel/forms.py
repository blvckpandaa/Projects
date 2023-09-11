from django.forms import forms
from .models import *
from django.forms import ModelForm,TextInput,Textarea,EmailInput
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['guest_name', 'email','request']

       
        widgets = {
            "guest_name": TextInput(attrs={
            'class':'form-control',
            "placeholder":"Your Name"
        }),
      
            "email": EmailInput(attrs={
            'class':'form-control',
            "placeholder":"Your Email"
        }),
      
            "request": Textarea(attrs={
            'class':'form-control',
            "placeholder":"Special Request"   
        }),
      
        
            }
        

