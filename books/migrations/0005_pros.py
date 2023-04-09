# Generated by Django 3.2.18 on 2023-03-30 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20230327_1958'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ind', models.SmallIntegerField(default=0)),
                ('author', models.CharField(max_length=70)),
                ('title', models.CharField(max_length=70)),
                ('image', models.ImageField(blank=True, null=True, upload_to='bks/list', verbose_name='Основное изображение')),
            ],
        ),
    ]