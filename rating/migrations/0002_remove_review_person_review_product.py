# Generated by Django 4.1.2 on 2022-11-10 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_shop_price'),
        ('rating', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='person',
        ),
        migrations.AddField(
            model_name='review',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='shop.shop'),
            preserve_default=False,
        ),
    ]