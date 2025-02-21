# Generated by Django 5.1.4 on 2025-01-31 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0004_notice_eng_attachments'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='content',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='notice',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='notice',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='notice_eng',
            name='content',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='notice_eng',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='notice_eng',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
