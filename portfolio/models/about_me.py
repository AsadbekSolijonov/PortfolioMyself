from django.db import models

from portfolio.models.home import TimestampModel


class AboutMe(TimestampModel):
    title = models.CharField(max_length=128)
    subject = models.CharField(max_length=128)
    content = models.TextField(max_length=1000)
    pic = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'{self.title}'
