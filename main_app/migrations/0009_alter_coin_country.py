# Generated by Django 4.2.2 on 2023-06-11 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_coin_country_bid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='country',
            field=models.CharField(choices=[('DOM', 'Dominican Republic'), ('USA', 'United States')], default='DOM', max_length=35),
        ),
    ]
