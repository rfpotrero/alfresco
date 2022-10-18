from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Reservations
from .forms import ReservationsForm


def home(request):
    return render(request, '../templates/home.html')


def menu(request):
    return render(request, '../templates/menu.html')


def contact(request):
    return render(request, '../templates/contact.html')


def make_reservation(request):
    """
    Capture and saves the information entered in the
    form.
    """
    if request.method == "POST":
        form = ReservationsForm(request.POST)
        if form.is_valid():
            time = request.POST.get('time_reservation')
            date = request.POST.get('date_reservation')
            form.instance.client = request.user
            # Double reservation verification based in User logged, time and date.
            duplicate_reservations = duplicate_reservations_verification(time, date, form)
            if len(duplicate_reservations) > 0:
                messages.error(request, 'There is an existing reservation')
                return render(request, '../templates/reservations.html',
                                       {'form': form})
            form.save()
            form_data = form.save()
            return render(request, '../templates/confirmed.html',
                                   {'form_data': form_data})

        return render(request, '../templates/reservations.html',
                               {'form': form})

    form = ReservationsForm
    return render(request, '../templates/reservations.html',
                            {'form': form})

@login_required
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

@login_required
def delete_reservation(request, reservation_code):
    """
    Delete an exsiting reservation
    """
    delete_reservation = Reservations.objects.get(
        reservation_code__exact=reservation_code)
    delete_reservation.delete()
    return redirect('client_reservations')

@login_required
def update_reservation(request, reservation_code):
    """
    Function to update an existing reservation
    """
    reservation = Reservations.objects.get(
        reservation_code__exact=reservation_code)
    form = ReservationsForm(request.POST or None, instance=reservation)
    if form.is_valid():
        time = request.POST.get('time_reservation')
        date = request.POST.get('date_reservation')
        form.instance.client = request.user
        # Double reservation verification based in User logged, time and date.
        duplicate_reservations = duplicate_reservations_verification(time, date, form)
        print(duplicate_reservations)
        if len(duplicate_reservations) > 0:
            messages.error(request, 'There is an existing reservation')
            return render(request, '../templates/update_reservation.html',
                                   {'form': form, 'reservation': reservation})
        form.save()
        form_data = form.save()
        return render(request, '../templates/confirmed.html',
                                   {'form_data': form_data})

    return render(request, '../templates/update_reservation.html',
                           {'reservation': reservation, 'form': form})

@login_required
def client_reservations(request):
    now = datetime.now()
    today = now.date()
    if request.user.is_authenticated:
        my_reservations = Reservations.objects.filter(client=request.user).filter(date_reservation__gte=today)
        return render(request, '../templates/client_reservations.html',
                               {'my_reservations': my_reservations})


def duplicate_reservations_verification(time, date, form):
    """
    Use to verify existing reservations. If the return object is >0
    a previous reservation is detected.
    """
    duplicate_reservations_number = Reservations.objects.filter(
        Q(time_reservation=time),
        Q(date_reservation=date),
        Q(client=form.instance.client)
    )
    return duplicate_reservations_number

def error_404(request, exception):
    return render(request, '../templates/error404.html')
