# Generated by Django 2.0.1 on 2018-08-17 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campusbuy', '0021_auto_20180817_1243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemadvert',
            name='Image',
        ),
    ]
