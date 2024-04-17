from django.db import models
from django.core.validators import MaxValueValidator


class Score(models.Model):
    name = models.CharField(max_length=50)
    value = models.IntegerField(validators=[MaxValueValidator(100)])

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-value']
