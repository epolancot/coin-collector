# Generated by Django 4.2.2 on 2023-06-11 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_alter_coin_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='condition',
            field=models.CharField(choices=[('M', 'Mint State'), ('V', 'Very Good'), ('G', 'Good'), ('F', 'Fair'), ('P', 'Poor')], default=('M', 'Mint State'), max_length=35),
        ),
    ]