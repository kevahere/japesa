# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-28 09:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('category', models.CharField(max_length=250)),
                ('reviews', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewer', models.CharField(max_length=250)),
                ('rating', models.PositiveIntegerField(default=0)),
                ('description', models.TextField(max_length=300)),
                ('likes', models.IntegerField(default=0)),
                ('pub_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
