# Generated by Django 3.2 on 2023-08-15 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_customuser_address'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='region',
            options={'ordering': ('name',)},
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True, verbose_name='email address'),
        ),
    ]
