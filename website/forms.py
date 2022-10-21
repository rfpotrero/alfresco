from django import forms
from .models import Reservations


class ReservationsForm(forms.ModelForm):
    class Meta:
        model = Reservations
        exclude = ('client', 'reservation_code')
        widgets = {

            'date_reservation': forms.DateInput(attrs={
                                                'class': 'form-control',
                                                'type': 'date'}),
            'time_reservation': forms.Select(attrs={'class': 'form-control'}),
            'name_client': forms.TextInput(attrs={'class': 'form-control'}),
            'phonenumber_client': forms.TextInput(attrs={
                                            'class': 'form-control',
                                            'type': 'tel'}),
            'email_client': forms.EmailInput(attrs={'class': 'form-control'}),
            'numberofpeople': forms.Select(attrs={'class':
                                                  'form-control'})
        }
