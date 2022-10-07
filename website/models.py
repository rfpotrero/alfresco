import uuid
from shortuuid.django_fields import ShortUUIDField
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Reservations(models.Model):
    """
    Model for client reservations
    """
    date = models.DateTimeField()
    name = models.CharField(max_length=100)
    phone = PhoneNumberField()
    email = models.EmailField()
    numberofpeople = models.IntegerField(default=2)
    reservation_code = ShortUUIDField(
        length=7,
        max_length=10,
        alphabet="abcdefg1234",
        editable=False)
    reservation_id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                                      editable=False)

    class Meta:
        ordering = ['-date']
        verbose_name_plural = "Reservations"

    def __str__(self):
        return self.name
