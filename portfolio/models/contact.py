from django.db import models

from portfolio.models.home import TimestampModel


class Contact(TimestampModel):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField(max_length=1000)

    def __str__(self):
        return f'{self.name}'


