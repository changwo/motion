# Generated by Django 3.0.3 on 2020-06-23 15:45

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200623_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='things_user_likes',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, default=list, size=None),
        ),
    ]
