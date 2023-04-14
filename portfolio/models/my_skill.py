from django.db import models

from portfolio.models.home import TimestampModel


class MySkills(TimestampModel):
    present = models.IntegerField()
    skill_name = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.skill_name}'
