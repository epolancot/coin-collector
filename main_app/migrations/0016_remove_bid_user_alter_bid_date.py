# Generated by Django 4.2.2 on 2023-06-11 20:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0015_alter_coin_condition'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='user',
        ),
        migrations.AlterField(
            model_name='bid',
            name='date',
            field=models.DateField(default=datetime.date(2023, 6, 11)),
        ),
    ]