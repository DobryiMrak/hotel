# Generated by Django 2.0 on 2020-02-19 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_checkin_date_chekin'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='checkin',
            options={'verbose_name': 'Заселение', 'verbose_name_plural': 'Заселения'},
        ),
    ]