from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from website.models import Reservations


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('reservation_list')
        else:
            messages.success(request,
                             ("There was an error. Please try agains"))
            return redirect('login')

    else:
        return render(request, 'authentication/login.html', {})


def reservation_list(request):
    now = datetime.now()
    today = now.date()
    reservation_list = Reservations.objects.filter(date__date=today)
    return render(request, 'authentication/reservation_list.html',
                           {'reservation_list': reservation_list})
