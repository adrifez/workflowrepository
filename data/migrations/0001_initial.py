# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-29 12:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('created', models.DateField(default=datetime.date.today)),
                ('tooltip', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Workflow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.CharField(default='', max_length=512)),
                ('views', models.IntegerField(default=0)),
                ('downloads', models.IntegerField(default=0)),
                ('versionInit', models.CharField(max_length=128)),
                ('client_ip', models.GenericIPAddressField()),
                ('keywords', models.CharField(default='', max_length=256)),
                ('json', models.TextField()),
                ('created', models.DateField(default=datetime.date.today)),
                ('category', models.ManyToManyField(to='data.Category')),
            ],
            options={
                'verbose_name_plural': 'Workflows',
            },
        ),
    ]
