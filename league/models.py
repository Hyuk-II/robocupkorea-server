from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from config.supabase_storage import SupabaseStorage


class League(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    attachments = models.JSONField(default=list, blank=True)

    def __str__(self):
        return self.id


class League_ENG(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    attachments = models.JSONField(default=list, blank=True)

    def __str__(self):
        return self.id
