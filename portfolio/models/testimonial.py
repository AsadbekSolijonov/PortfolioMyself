from django.db import models

from portfolio.models.home import TimestampModel


class Testimonial(TimestampModel):
    pic = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=128)
    position = models.CharField(max_length=50)
    description = models.TextField(max_length=128)

    def __str__(self):
        return f'{self.name}'
