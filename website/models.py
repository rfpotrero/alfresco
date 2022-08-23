import uuid
from django.db import models
from django.contrib.auth.models import User


class Reservations(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()
    numberofpeople = models.IntegerField(default=2)
    reservation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        ordering = ['-date']
        verbose_name_plural = "Reservations"

    def __str__(self):
        return self.name

