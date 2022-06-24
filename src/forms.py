from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import MovingDetails

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name....', }),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name..'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username..'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email...'}),
        }
        
        
# user form
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', ]

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name..', }),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name..'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email...'}),
        }
        
        
# create cost form
class CostForm(forms.ModelForm):
    class Meta:
        model = MovingDetails
        fields = ['address', 'destination', 'luggage_size', 'relocating_on']
        
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Address...', 'required': 'required'}),
            'destination': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Destination -where to...', 'required': 'required'}),
            'luggage_size': forms.Select(attrs={'class': 'form-control', 'placeholder': 'My Luggage Size...', 'required': 'required'}),
            'relocating_on': forms.DateInput(attrs={'type': 'date','class': 'form-control', 'placeholder': 'when are you planning...', 'required': 'required'}),
        }