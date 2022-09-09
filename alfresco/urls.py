"""alfresco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from website.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_home, name='home'),
    path('home', get_home, name='home'),
    path('menu', get_menu, name='menu'),
    path('contact', get_contact, name='contact'),
    path('reservations', get_reservations, name='reservations'),
    path('search_reservation', get_search_reservation, name='search_reservation'),
    path('delete_reservation/<reservation_code>', get_delete_reservation, name='delete_reservation'),
]
