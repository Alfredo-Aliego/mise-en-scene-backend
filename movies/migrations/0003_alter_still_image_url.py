# Generated by Django 4.2.4 on 2023-09-29 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_still_remove_movie_id_alter_movie_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='still',
            name='image_url',
            field=models.CharField(max_length=1000),
        ),
    ]