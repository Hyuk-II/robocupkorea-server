from django.db import models

class Event(models.Model):
    create_date=models.DateTimeField()