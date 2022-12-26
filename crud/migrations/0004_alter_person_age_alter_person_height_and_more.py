# Generated by Django 4.1.2 on 2022-11-08 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_person_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='person',
            name='height',
            field=models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Рост'),
        ),
        migrations.AlterField(
            model_name='person',
            name='weight',
            field=models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Вес'),
        ),
    ]
# 