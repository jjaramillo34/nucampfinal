# Generated by Django 4.0.6 on 2022-08-10 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_home_class_css'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='class_css',
        ),
    ]
