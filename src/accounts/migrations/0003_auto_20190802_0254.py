# Generated by Django 2.2.4 on 2019-08-01 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190802_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'r_donate'), (1, 'g_donate')], null=True),
        ),
    ]