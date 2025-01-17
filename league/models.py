from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.contrib.postgres.fields import ArrayField


class Attachment(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    document = models.FileField("첨부 파일", upload_to="files/")

    def __str__(self):
        return self.id


class League(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    date = models.DateField()
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    content = models.TextField()
    attachments = ArrayField(models.CharField(max_length=50), default=list)

    def __str__(self):
        return self.title


@receiver(post_delete, sender=League)
def delete_related_attachments(sender, instance, **kwargs):
    Attachment.objects.filter(id__in=instance.attachments).delete()


@receiver(post_delete, sender=Attachment)
def delete_attachment_file(sender, instance, **kwargs):
    if instance.document and instance.document.path:
        instance.document.delete(save=False)
