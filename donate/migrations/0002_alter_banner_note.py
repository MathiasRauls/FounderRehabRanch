# Generated by Django 4.0.1 on 2022-07-16 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='note',
            field=models.CharField(default='Make Banner Image 2000px X 700px', editable=False, max_length=100),
        ),
    ]