# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-04 12:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blocks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Html',
            fields=[
                ('block_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blocks.Block')),
                ('code', models.TextField(blank=True, verbose_name='Code')),
            ],
            options={
                'verbose_name': 'HTML Block',
                'verbose_name_plural': 'HTML Blocks',
                'manager_inheritance_from_future': True,
            },
            bases=('blocks.block',),
        ),
    ]
