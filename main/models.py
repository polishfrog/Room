from django.db import models

# Create your models here.

class ConferenceRoom(models.Model):
    name = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()
    projector_availability = models.BooleanField(default=True)