# Generated by Django 3.1.7 on 2023-02-18 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspaper',
            name='publish_date',
            field=models.DateField(unique=True),
        ),
    ]
