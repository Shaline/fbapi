# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-23 10:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FacebookLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label_id', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FacebookPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.TextField()),
                ('original_id', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook_id', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='facebooklabel',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fbdata.User'),
        ),
        migrations.AddField(
            model_name='facebooklabel',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fbdata.FacebookPage'),
        ),
    ]
