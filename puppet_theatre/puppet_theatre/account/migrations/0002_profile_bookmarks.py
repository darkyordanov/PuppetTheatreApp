# Generated by Django 5.0.6 on 2024-05-25 09:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('grade', models.PositiveSmallIntegerField(choices=[(1, '1-ви клас'), (2, '2-ви клас'), (3, '3-ти клас'), (4, '4-ти клас'), (5, '5-ти клас'), (6, '6-ти клас'), (7, '7-ми клас'), (8, '8-ми клас'), (9, '9-ти клас'), (10, '10-ти клас'), (11, '11-ти клас'), (12, '12-ти клас')])),
                ('user', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bookmarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
