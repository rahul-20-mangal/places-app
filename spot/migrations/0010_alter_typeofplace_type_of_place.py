# Generated by Django 3.2 on 2021-04-15 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spot', '0009_auto_20210413_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typeofplace',
            name='type_of_place',
            field=models.CharField(default='Not Mentioned', max_length=200),
        ),
    ]