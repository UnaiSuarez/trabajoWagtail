# Generated by Django 3.2.11 on 2022-02-08 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pelis', '0003_auto_20220201_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='nombre',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
