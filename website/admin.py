from django.contrib import admin
from .models import Reservations

#admin.site.register(Reservations)

@admin.register(Reservations)
class ReservationsAdmin(admin.ModelAdmin):
    list_display = ('date_reservation', 'reservation_code')
    ordering = ('date_reservation',)