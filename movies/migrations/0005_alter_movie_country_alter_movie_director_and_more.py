# Generated by Django 4.2.4 on 2023-10-04 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_alter_still_imdb_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='country',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(max_length=1000),
        ),
    ]