# Generated by Django 3.1.7 on 2021-04-03 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
