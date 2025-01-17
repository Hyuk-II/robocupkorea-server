from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os


class Attachment(models.Model):
    document = models.FileField("첨부 파일", upload_to="notices/files/")
    name = models.CharField(max_length=255, blank=True)

    def save(self, *args, **kwargs):
        if self.document and not self.name:
            self.name = os.path.basename(self.document.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Notice(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    date = models.DateField()
    author = models.CharField(max_length=50)
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
    if instance.document and instance.document.path:
        instance.document.delete(save=False)
