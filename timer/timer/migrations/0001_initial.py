# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-11 08:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Timer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.IntegerField(max_length=10, verbose_name='Timer Duration')),
                ('is_completed', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('started', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
