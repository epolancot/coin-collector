# Generated by Django 4.2.2 on 2023-06-10 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='img',
            field=models.TextField(default='../static/images/default-coin-img.gif', max_length=300),
        ),
    ]
