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
from django.urls import path, include
from website import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('allauth.urls')),
    path('home', views.home, name='home'),
    path('menu', views.menu, name='menu'),
    path('contact', views.contact, name='contact'),
    path('reservations', views.reservations, name='reservations'),
    path('client_reservations', views.client_reservations, name="client_reservations"),
    path('search_reservation', views.get_search_reservation,
         name='search_reservation'),
    path('delete_reservation/<reservation_code>', views.get_delete_reservation,
         name='delete_reservation'),
    path('update_reservation/<reservation_code>', views.update_reservation,
         name='update_reservation'),
    path('business_login/', include('django.contrib.auth.urls')),
    path('business_login/', include('business_login.urls')),
]


handler404 = 'website.views.error_404'
