from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Reservations, Client
from .forms import ReservationsForm

def home(request):
    return render(request, '../templates/home.html')


def menu(request):
    return render(request, '../templates/menu.html')


def contact(request):
    return render(request, '../templates/contact.html')


def reservations(request):
    """
    This fuction capture and saves the information entered in the
    form.
    """
    if request.method == "POST":
        form = ReservationsForm(request.POST)
        if form.is_valid():
            form.save()
            form_data = form.save()
            return render(request, '../templates/confirmed.html',
                                   {'form_data': form_data})
        print(form.errors)
    else:
        form = ReservationsForm
        return render(request, '../templates/reservations.html',
                               {'form': form})


def get_search_reservation(request):
    """
    Search for existing reservation using the reservation code.
    Raise an error if the code does not exist.
    """
    if request.method == "POST":
        try:
            searched = request.POST['searched']
            print(searched)
            reservation = Reservations.objects.get(
                reservation_code__exact=searched)
            print(reservation.phone)
            return render(request, '../templates/search_reservation.html',
                                   {'searched': searched,
                                    'reservation': reservation})
        except Reservations.DoesNotExist:
            messages.error(request, 'Reservation Not found')
            return redirect('reservations')


def get_delete_reservation(request, reservation_code):
    delete_reservation = Reservations.objects.get(
        reservation_code__exact=reservation_code)
    delete_reservation.delete()
    return redirect('reservations')


def get_update_reservation(request, reservation_code):
    reservation = Reservations.objects.get(
        reservation_code__exact=reservation_code)
    form = ReservationForm(request.POST or None, instance=reservation)
    if form.is_valid():
        form.save()
        return render(request, '../templates/search_reservation.html',
                               {'reservation': reservation})  
    print(form.errors)
    return render(request, '../templates/update_reservation.html',
                           {'reservation': reservation, 'form': form})


def error_404(request, exception):
    return render(request, '../templates/error404.html')
