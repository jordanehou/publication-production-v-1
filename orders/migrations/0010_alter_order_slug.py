# Generated by Django 3.2.20 on 2023-07-13 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_order_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='slug',
            field=models.SlugField(default='1', max_length=200),
        ),
    ]