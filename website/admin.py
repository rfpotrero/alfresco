from django.contrib import admin
from .models import Reservations

#admin.site.register(Reservations)

@admin.register(Reservations)
class ReservationsAdmin(admin.ModelAdmin):
    list_display = ('name_client', 'date_reservation','time_reservation', 'reservation_code')
    ordering = ('date_reservation',)