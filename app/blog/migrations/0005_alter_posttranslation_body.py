# Generated by Django 4.0.6 on 2022-08-05 02:08

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_options_alter_posttranslation_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posttranslation',
            name='body',
            field=tinymce.models.HTMLField(blank=True),
        ),
    ]