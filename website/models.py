from shortuuid.django_fields import ShortUUIDField
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


GUESTS = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
)

TIME = (
    ('17:00', '17:00'),
    ('18:00', '18:00'),
    ('19:00', '19:00'),
    ('20:00', '20:00'),
    ('21:00', '21:00'),
    ('22:00', '22:00'),
)


class Reservations(models.Model):
    """
    Model for client reservations
    """

    date_reservation = models.DateField(max_length=30)
    time_reservation = models.CharField(max_length=30,
                                        choices=TIME, default='18:00')
    client = models.ForeignKey(User, related_name="reservations",
                               on_delete=models.SET_NULL, null=True)
    name_client = models.CharField(max_length=100)
    email_client = models.EmailField(max_length=200)
    phonenumber_client = PhoneNumberField()
    numberofpeople = models.CharField(max_length=2,
                                      choices=GUESTS, default='2')
    reservation_code = ShortUUIDField(
        length=7,
        max_length=10,
        alphabet="abcdefg1234",
        editable=False)

    class Meta:
        verbose_name_plural = "Reservations"
