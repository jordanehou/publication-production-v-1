# Generated by Django 3.2.20 on 2023-07-10 02:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0017_courseproposal_moduleproposal_subproposal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courseproposal',
            old_name='course',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='subproposal',
            old_name='subject',
            new_name='name',
        ),
    ]
