from django.db import models
from django.utils import timezone

from datetime import timedelta

# Create your models here.


class Tournament(models.Model):
    tournament_name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    sport = models.CharField(max_length=255)
    date_created = models.DateTimeField(default=timezone.now())
    tournament_start = models.DateTimeField(
        default=timezone.now, auto_now=False, auto_now_add=False
    )
    tournament_end = models.DateTimeField(
        default=timezone.now() + timedelta(days=5), auto_now=False, auto_now_add=False
    )
    bracketing_system = models.CharField(max_length=255)
    # requirements = models.ArrayField()
