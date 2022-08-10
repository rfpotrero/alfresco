from django.shortcuts import render


def get_home(request):
    return render(request, '../templates/home.html')


def get_menu(request):
    return render(request, '../templates/menu.html')


def get_contact(request):
    return render(request, '../templates/contact.html')


def get_reservations(request):
    return render(request, '../templates/reservations.html')