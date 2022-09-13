from django.forms import ModelForm
from .models import Reservations

class ReservationForm(ModelForm):
    class Meta:
        model = Reservations
        fields = ('date', 'name', 'phone', 'email', 'numberofpeople') 


