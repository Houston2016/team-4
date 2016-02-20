# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CardModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=52)),
                ('weight', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CardSubmissionModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('submission', models.ManyToManyField(to='Ranking.CardModel')),
            ],
        ),
        migrations.CreateModel(
            name='MatteModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=52)),
                ('description', models.CharField(max_length=240)),
                ('submissions', models.ManyToManyField(to='Ranking.CardSubmissionModel')),
            ],
        ),
        migrations.CreateModel(
            name='Themes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=52)),
                ('description', models.CharField(max_length=240)),
            ],
        ),
        migrations.AddField(
            model_name='mattemodel',
            name='themes',
            field=models.ManyToManyField(to='Ranking.Themes'),
        ),
    ]
