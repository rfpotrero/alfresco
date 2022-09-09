from re import search
from django.shortcuts import render
from .forms import ReservationForm
from .models import Reservations


def get_home(request):
    return render(request, '../templates/home.html')


def get_menu(request):
    return render(request, '../templates/menu.html')


def get_contact(request):
    return render(request, '../templates/contact.html')


def get_reservations(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            form_data = form.save()
            return render(request, '../templates/confirmed.html', {'form_data': form_data})
    else:
        form = ReservationForm
        return render(request, '../templates/reservations.html', {'form': form})


def get_search_reservation(request):
    if request.method == "POST":  
        searched = request.POST['searched']  
        print(searched)
        reservation = Reservations.objects.get(reservation_code__exact= searched)
        print(reservation.phone)
        return render(request, '../templates/search_reservation.html', {'searched': searched, 'reservation': reservation})