# Generated by Django 3.2.18 on 2023-03-21 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.CharField(max_length=70)),
                ('trans', models.CharField(max_length=70)),
                ('rus', models.CharField(max_length=150)),
            ],
        ),
    ]
