# Generated by Django 3.2.18 on 2023-03-28 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_todo_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
            ],
        ),
    ]
