# Generated by Django 3.2.9 on 2021-12-16 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='is_crawled',
            field=models.BooleanField(default=False),
        ),
    ]
