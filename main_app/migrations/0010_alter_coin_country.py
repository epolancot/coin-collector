# Generated by Django 4.2.2 on 2023-06-11 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_alter_coin_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='country',
            field=models.CharField(max_length=35),
        ),
    ]
