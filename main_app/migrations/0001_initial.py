# Generated by Django 4.2.2 on 2023-06-10 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.TextField(max_length=300)),
                ('denomination', models.CharField(max_length=35)),
                ('circulated', models.BooleanField()),
                ('year', models.IntegerField()),
                ('for_sale', models.BooleanField()),
                ('condition', models.CharField(max_length=35)),
                ('details', models.TextField(max_length=500)),
            ],
        ),
    ]
