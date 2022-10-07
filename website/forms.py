from django import forms
from django.forms import ModelForm
from phonenumber_field.formfields import PhoneNumberField
from .models import Reservations



class ReservationForm(ModelForm):
    """
    Form to capture reservations from clients.
    """
    class Meta:
        model = Reservations
        phone = PhoneNumberField()
        fields = ('date', 'name', 'phone', 'email', 'numberofpeople')
        widgets = {
            'date': forms.DateTimeInput(attrs={'class': 'form-control'},
                                        format='%Y-%m-%d %H:%M'),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'numberofpeople': forms.NumberInput(attrs={'class':
                                                       'form-control'})
        }
