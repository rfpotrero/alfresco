from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReservationForm


def get_home(request):
    return render(request, '../templates/home.html')


def get_menu(request):
    return render(request, '../templates/menu.html')


def get_contact(request):
    return render(request, '../templates/contact.html')


def get_reservations(request):
    reserved = False
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/reservations?reserved=True')
    else:
        form = ReservationForm
        if 'reserved' in request.GET:
            reserved = True

    return render(request, '../templates/reservations.html', {'form': form, 'reserved': reserved})
