# Generated by Django 3.2.20 on 2023-07-11 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_orderitem_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='owner',
        ),
    ]
