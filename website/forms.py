from django import forms
from django.forms import ModelForm
from .models import Reservations

class ReservationForm(ModelForm):
    class Meta:
        model = Reservations
        fields = ('date', 'name', 'phone', 'email', 'numberofpeople')
        widgets = {
            'date': forms.DateTimeInput(format='%Y-%m-%d %H:%M')
        }

