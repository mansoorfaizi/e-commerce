from django.db import models
from .timestamp import TimeStampedModel


class Category(TimeStampedModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name