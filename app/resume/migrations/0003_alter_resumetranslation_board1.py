# Generated by Django 4.0.6 on 2022-08-06 15:01

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_alter_resumetranslation_board1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumetranslation',
            name='board1',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=200), size=None), size=None),
        ),
    ]