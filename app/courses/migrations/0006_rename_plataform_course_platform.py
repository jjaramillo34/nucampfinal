# Generated by Django 4.0.6 on 2022-07-29 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_course_plataform'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='plataform',
            new_name='platform',
        ),
    ]
