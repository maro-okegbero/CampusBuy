# Generated by Django 2.0.1 on 2018-07-26 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campusbuy', '0012_auto_20180726_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemadvert',
            name='Asking_Price',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
