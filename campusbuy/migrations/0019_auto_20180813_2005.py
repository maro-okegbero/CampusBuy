# Generated by Django 2.0.1 on 2018-08-13 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campusbuy', '0018_auto_20180813_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemadvert',
            name='Phone_Number',
            field=models.CharField(help_text='<p style="color: red; font: italic 12px tahoma;">Please input a working line that you can be contacted with</p>', max_length=11),
        ),
    ]
