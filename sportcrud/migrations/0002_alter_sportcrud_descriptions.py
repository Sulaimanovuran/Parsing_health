# Generated by Django 4.1.2 on 2022-11-09 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportcrud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sportcrud',
            name='descriptions',
            field=models.CharField(max_length=300),
        ),
    ]