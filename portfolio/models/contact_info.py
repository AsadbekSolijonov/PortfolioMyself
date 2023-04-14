from django.db import models

from portfolio.models.home import TimestampModel


class ContactInfo(TimestampModel):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f'{self.name}'


