# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-05 06:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Generation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generation_name', models.CharField(max_length=128)),
                ('generation_number', models.PositiveSmallIntegerField(unique=True)),
                ('next_generation', models.NullBooleanField()),
                ('available_from', models.DateTimeField()),
                ('available_until', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Painting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, null=True)),
                ('published', models.DateTimeField(auto_now=True)),
                ('summary', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, upload_to='paintings')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('generation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='xyz.Generation')),
                ('parents', models.ManyToManyField(blank=True, null=True, related_name='_painting_parents_+', to='xyz.Painting')),
            ],
        ),
    ]
