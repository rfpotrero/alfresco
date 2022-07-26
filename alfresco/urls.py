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

from django.urls import path, include
from django.contrib import admin
from website import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('allauth.urls')),
    path('home', views.home, name='home'),
    path('menu', views.menu, name='menu'),
    path('contact', views.contact, name='contact'),
    path('reservations', views.client_reservations,
         name="client_reservations"),
    path('make_reservation', views.make_reservation, name='make_reservation'),
    path('delete_reservation/<reservation_code>', views.delete_reservation,
         name='delete_reservation'),
    path('update_reservation/<reservation_code>', views.update_reservation,
         name='update_reservation'),
]


HANDLER404 = 'website.views.error_404'
