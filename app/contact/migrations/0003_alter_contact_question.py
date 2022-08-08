# Generated by Django 4.0.6 on 2022-07-28 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_rename_contactpage_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='question',
            field=models.CharField(choices=[('0', "Select a service package you're interested in..."), ('1', 'Basic'), ('2', 'Standard'), ('3', 'Premium'), ('4', 'Not sure')], max_length=1),
        ),
    ]