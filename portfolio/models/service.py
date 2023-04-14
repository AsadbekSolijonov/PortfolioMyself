from django.db import models

from portfolio.models.home import TimestampModel


class Services(TimestampModel):
    icons = models.CharField(max_length=80)
    service_name = models.CharField(max_length=50)
    content = models.TextField(max_length=150)

    def __str__(self):
        return f'{self.service_name}'
