# Generated by Django 2.0.1 on 2008-01-05 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campusbuy', '0030_auto_20080105_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='image',
            field=models.ImageField(default='gadgets.png', upload_to='uploads'),
            preserve_default=False,
        ),
    ]
