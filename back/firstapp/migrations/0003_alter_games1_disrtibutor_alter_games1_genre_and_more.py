# Generated by Django 4.2.6 on 2023-10-14 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_games1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games1',
            name='disrtibutor',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='games1',
            name='genre',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='games1',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='games1',
            name='price',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='games1',
            name='production',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='games1',
            name='publication_data',
            field=models.CharField(max_length=20),
        ),
    ]