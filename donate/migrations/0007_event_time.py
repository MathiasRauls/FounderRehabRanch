# Generated by Django 4.1.3 on 2022-11-25 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0006_event_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.CharField(default='9AM', max_length=10),
        ),
    ]