from django import forms
from django.forms import ModelForm
from .models import Reservations


class ReservationForm(ModelForm):
    class Meta:
        model = Reservations
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
