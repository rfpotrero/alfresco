from django import forms
from .models import Reservations


class ReservationsForm(forms.ModelForm):
    class Meta:
        model = Reservations
        fields = ('date_reservation', 'time_reservation', 'numberofpeople')
        widgets = {
            'date_reservation': forms.DateInput(attrs={
                                                'class': 'form-control',
                                                'type': 'date'}),
            'time_reservation': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'numberofpeople': forms.Select(attrs={'class':
                                                  'form-control'})
        }
