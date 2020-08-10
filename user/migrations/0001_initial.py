# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-10 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phonenum', models.CharField(max_length=16, unique=True, verbose_name='手机号')),
                ('nickname', models.CharField(db_index=True, max_length=20, verbose_name='昵称')),
                ('gender', models.CharField(choices=[('male', '男性'), ('female', '女性')], default='male', max_length=10, verbose_name='性别')),
                ('birthday', models.DateField(default='2000-01-01', verbose_name='出生日')),
                ('avatar', models.CharField(max_length=256, verbose_name='个人形象 URL')),
                ('location', models.CharField(choices=[('北京', '北京'), ('上海', '上海'), ('深圳', '深圳'), ('武汉', '武汉'), ('成都', '成都'), ('西安', '西安'), ('沈阳', '沈阳')], default='上海', max_length=10, verbose_name='常居地')),
            ],
        ),
    ]
