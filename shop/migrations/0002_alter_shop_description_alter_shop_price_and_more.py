# Generated by Django 4.1.2 on 2022-11-09 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='description',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='shop',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='title',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
