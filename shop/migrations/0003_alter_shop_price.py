# Generated by Django 4.1.2 on 2022-11-09 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_shop_description_alter_shop_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Возраст'),
        ),
    ]
