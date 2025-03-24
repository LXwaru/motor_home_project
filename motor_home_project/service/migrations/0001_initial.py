# Generated by Django 5.1.7 on 2025-03-24 21:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("inventory", "0003_remove_motorhome_price_motorhome_condition_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ServicePerson",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=100)),
                ("phone", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="ServiceTicket",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("service_date", models.DateField()),
                ("service_description", models.TextField()),
                ("service_price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("is_completed", models.BooleanField(default=False)),
                ("is_paid", models.BooleanField(default=False)),
                ("is_warranty", models.BooleanField(default=False)),
                (
                    "motor_home",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inventory.motorhome",
                    ),
                ),
                (
                    "service_person",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="service.serviceperson",
                    ),
                ),
            ],
        ),
    ]
