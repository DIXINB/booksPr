# Generated by Django 3.2.18 on 2023-03-25 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_dict'),
    ]

    operations = [
        migrations.AddField(
            model_name='hist',
            name='ind',
            field=models.SmallIntegerField(default=0),
        ),
    ]
