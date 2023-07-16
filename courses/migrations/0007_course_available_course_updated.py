# Generated by Django 4.2.2 on 2023-07-05 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_alter_course_options_alter_subject_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='course',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
