# Generated by Django 2.2.6 on 2019-12-28 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ml', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='other_predictions',
        ),
    ]
