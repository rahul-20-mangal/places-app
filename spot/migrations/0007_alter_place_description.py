# Generated by Django 3.2 on 2021-04-11 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spot', '0006_alter_place_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]
