# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-04 12:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'Unpublish'), (2, 'Publish')], db_index=True, default=1, help_text='Only admins can see drafts.', verbose_name='Status')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('publish_date', models.DateTimeField(blank=True, db_index=True, help_text="With Published chosen, won't be shown until this time", null=True, verbose_name='Published from')),
                ('expiry_date', models.DateTimeField(blank=True, help_text="With Published chosen, won't be shown after this time", null=True, verbose_name='Expires on')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='Title')),
                ('show_title', models.BooleanField(default=False, verbose_name='Show title')),
                ('section', models.CharField(blank=True, choices=[('sidebar', 'Sidebar'), ('footer', 'Footer')], max_length=255, null=True, verbose_name='Section')),
                ('wrapper_css_class', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='Wrapper css class')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_blocks.block_set+', to='contenttypes.ContentType')),
            ],
            options={
                'manager_inheritance_from_future': True,
            },
        ),
    ]