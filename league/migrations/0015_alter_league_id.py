# Generated by Django 5.1.4 on 2025-01-26 09:12

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0014_remove_league_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='league',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
