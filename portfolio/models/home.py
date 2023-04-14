from django.db import models


class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Home(TimestampModel):
    greating = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    content = models.TextField(max_length=1000)

    def __str__(self):
        return f'{self.title}'
