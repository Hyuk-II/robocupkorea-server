from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models.signals import post_delete
from django.dispatch import receiver
from config.supabase_storage import SupabaseStorage


class Event(models.Model):
    id = models.CharField(max_length=50, primary_key=True, null=False)
    title = models.CharField(max_length=50)

    start_date = models.DateField()
    end_date = models.DateField()

    location = models.CharField(max_length=50)
    map = models.CharField(max_length=255)
    register = models.CharField(max_length=255)

    others = models.JSONField(blank=True, default=list)

    image_top = models.ImageField(
        storage=SupabaseStorage(), upload_to="kor/posters/top/", blank=True
    )
    image_bottom = models.ImageField(
        storage=SupabaseStorage(), upload_to="kor/posters/bottom/", blank=True
    )

    leagues = ArrayField(models.CharField(max_length=50), blank=True, default=list)

    def __str__(self):
        return self.title


class Event_ENG(models.Model):
    id = models.CharField(max_length=50, primary_key=True, null=False)
    title = models.CharField(max_length=50)

    start_date = models.DateField()
    end_date = models.DateField()

    location = models.CharField(max_length=50)
    map = models.CharField(max_length=255)
    register = models.CharField(max_length=255)

    others = models.JSONField(blank=True, default=list)

    image_top = models.ImageField(
        storage=SupabaseStorage(), upload_to="eng/posters/top/", blank=True
    )
    image_bottom = models.ImageField(
        storage=SupabaseStorage(), upload_to="eng/posters/bottom/", blank=True
    )

    leagues = ArrayField(models.CharField(max_length=50), blank=True, default=list)

    def __str__(self):
        return self.title


@receiver(post_delete, sender=Event)
def delete_event_files(sender, instance, **kwargs):
    if instance.image_top:
        instance.image_top.delete(save=False)
    if instance.image_bottom:
        instance.image_bottom.delete(save=False)


@receiver(post_delete, sender=Event_ENG)
def delete_event_files(sender, instance, **kwargs):
    if instance.image_top:
        instance.image_top.delete(save=False)
    if instance.image_bottom:
        instance.image_bottom.delete(save=False)
