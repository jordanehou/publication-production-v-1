# Generated by Django 3.2.20 on 2023-07-10 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0015_alter_subject_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]