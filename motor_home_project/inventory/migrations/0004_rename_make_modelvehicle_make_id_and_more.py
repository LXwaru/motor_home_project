# Generated by Django 5.1.7 on 2025-03-25 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0003_remove_motorhome_price_motorhome_condition_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="modelvehicle",
            old_name="make",
            new_name="make_id",
        ),
        migrations.RenameField(
            model_name="motorhome",
            old_name="model",
            new_name="model_id",
        ),
    ]
