# Generated by Django 4.2.2 on 2023-06-11 20:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0018_alter_bid_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Date'),
        ),
    ]
