# Generated by Django 2.0 on 2020-02-20 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_checkin_date_checkout'),
    ]

    operations = [
        migrations.AddField(
            model_name='resedent',
            name='in_bucket',
            field=models.BooleanField(default=True),
        ),
    ]
