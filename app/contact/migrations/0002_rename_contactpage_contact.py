# Generated by Django 4.0.6 on 2022-07-22 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContactPage',
            new_name='Contact',
        ),
    ]