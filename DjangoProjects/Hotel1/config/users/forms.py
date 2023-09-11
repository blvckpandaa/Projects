from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

class SignUpForm(UserCreationForm):
  username = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label='Write your username')
  password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input'}), label='Write your password')
  password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input'}), label='Write your repeat password')
  class Meta:
    model = User
    fields = ['username', 'password1', 'password2']



  

class SignInForm(AuthenticationForm):
  username = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label='Write your username')
  password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input'}), label='Write your password')
  model = User
  fields = ['username' 'password']




class EditProfile(forms.ModelForm):
  username = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label='Write your username')
  class Meta:
    model = User
    fields=['username']



class ChangePasswordForm(PasswordChangeForm):
  old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input'}), label='Write your old password')
  new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input'}), label='Write your new password')
  new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input'}), label='Write your repeat password')
  class Meta:
    model = User
    fields = ['old_password', 'new_password1', 'new_password2']



