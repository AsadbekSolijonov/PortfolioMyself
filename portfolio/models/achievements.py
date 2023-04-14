from django.db import models

from portfolio.models.home import TimestampModel


class Achievements(TimestampModel):
    icon = models.CharField(max_length=128)
    count = models.IntegerField()
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'
