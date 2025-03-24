# Generated by Django 5.1.7 on 2025-03-24 20:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Make",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Model",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                (
                    "make",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="inventory.make"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MotorHome",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("vin", models.CharField(max_length=17, unique=True)),
                ("year", models.IntegerField()),
                ("color", models.CharField(max_length=100)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="motor_homes/"),
                ),
                ("is_new", models.BooleanField(default=True)),
                ("for_sale", models.BooleanField(default=True)),
                ("is_sold", models.BooleanField(default=False)),
                ("sold_date", models.DateField(blank=True, null=True)),
                (
                    "model",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inventory.model",
                    ),
                ),
            ],
        ),
    ]
