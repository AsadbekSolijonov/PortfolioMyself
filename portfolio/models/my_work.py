from django.db import models

from portfolio.models.home import TimestampModel


class MyWork(TimestampModel):
    work_name = models.CharField(max_length=128)
    pic = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=256)

    def __str__(self):
        return f'{self.work_name}'
