from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from config.supabase_storage import SupabaseStorage
import os, uuid


class Attachment(models.Model):
    document = models.FileField(
        "첨부 파일", storage=SupabaseStorage(), upload_to="leauges/files/"
    )
    name = models.CharField(max_length=255, blank=True)
    size = models.PositiveIntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.document and not self.name:
            self.name = os.path.basename(self.document.name)
        if self.document:
            self.size = self.document.size
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class League(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField()
    title = models.CharField(max_length=50)
    content = models.TextField()
    attachments = models.ManyToManyField(Attachment, blank=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.attachments.all().delete()
        super().delete(*args, **kwargs)


@receiver(post_delete, sender=Attachment)
def delete_attachment_file(sender, instance, **kwargs):
    if instance.document:
        instance.document.delete(save=False)
