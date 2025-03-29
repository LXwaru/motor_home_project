# Generated by Django 5.1.7 on 2025-03-29 05:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("service", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="serviceticket",
            name="service_person",
        ),
        migrations.AddField(
            model_name="serviceticket",
            name="service_provider",
            field=models.ForeignKey(
                blank=True,
                limit_choices_to={"is_service_provider": True},
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="service_tickets",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
