from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from config.supabase_storage import SupabaseStorage
import uuid


class Notice(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    date = models.DateField(null=True)
    title = models.CharField(max_length=255, blank=True)
    content = models.CharField(max_length=255, blank=True)

    attachments = models.JSONField(default=list, blank=True)

    def __str__(self):
        return self.title


class Notice_ENG(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    date = models.DateField(null=True)
    title = models.CharField(max_length=255, blank=True)
    content = models.CharField(max_length=255, blank=True)

    attachments = models.JSONField(default=list, blank=True)

    def __str__(self):
        return self.title
