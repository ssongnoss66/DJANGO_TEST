# Generated by Django 3.2.18 on 2023-04-12 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]