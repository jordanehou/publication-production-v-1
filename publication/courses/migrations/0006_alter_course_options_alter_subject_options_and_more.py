# Generated by Django 4.2.2 on 2023-07-05 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_rename_creer_par_module_owner_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'ordering': ('name',), 'verbose_name': 'subject', 'verbose_name_plural': 'subjects'},
        ),
        migrations.AddField(
            model_name='course',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterIndexTogether(
            name='course',
            index_together={('id', 'slug')},
        ),
    ]
