# Generated by Django 4.2 on 2023-04-26 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("items", "0003_item_supply_ability_item_supply_period"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="supply_ability_length",
            field=models.CharField(default="", max_length=255),
        ),
        migrations.AddField(
            model_name="item",
            name="supply_ability_unit",
            field=models.CharField(default="", max_length=255),
        ),
    ]
