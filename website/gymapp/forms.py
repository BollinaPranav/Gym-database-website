from django import forms
from django.forms import ModelForm
from .models import Client, Trainers

# Create a Trainers form
class TrainersForm(ModelForm):
    class Meta:
        model = Trainers
        fields = ('name', 'address', 'phonenumber', 'email')
        labels = {
            'name': '',
            'address': '',
            'phonenumber': '',
            'email': ''
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Name of the trainer', 'name':'name'}),
            'address':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Trainer address', 'name': 'address'}),
            'phonenumber':forms.TextInput(attrs={'class':'form-control','placeholder':'Phone number', 'name':'phonenumber'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email address (abc12@efg.hij)', 'name':'email'})
        }


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'dateofjoining', 'phonenumber', 'Amountdue','trainer', 'clientimage')
        labels = {
            'name': '',
            'dateofjoining': '',
            'phonenumber': '',
            'Amountdue': '',
            'trainer':'Select Trainer:',
            'clientimage':''
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Name of the Client', 'name':'name'}),
            'dateofjoining':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Date of joining', 'name': 'dateofjoining'}),
            'phonenumber': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number', 'name': 'phonenumber'}),
            'Amountdue': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Amount Due', 'name': 'amountdue'}),
            'trainer': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Trainer name', 'name': 'trainer'}),
        }