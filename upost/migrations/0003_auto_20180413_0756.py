# Generated by Django 2.0.2 on 2018-04-13 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upost', '0002_auto_20180404_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.CharField(max_length=20),
        ),
    ]