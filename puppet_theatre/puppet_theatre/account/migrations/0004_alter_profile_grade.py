# Generated by Django 5.0.6 on 2024-05-26 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_profile_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='grade',
            field=models.PositiveSmallIntegerField(choices=[(1, '1-ви клас'), (2, '2-ви клас'), (3, '3-ти клас'), (4, '4-ти клас'), (5, '5-ти клас'), (6, '6-ти клас'), (7, '7-ми клас'), (8, '8-ми клас'), (9, '9-ти клас'), (10, '10-ти клас'), (11, '11-ти клас'), (12, '12-ти клас')], default=2),
            preserve_default=False,
        ),
    ]