# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityDict',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='城市')),
                ('desc', models.CharField(max_length=200, verbose_name='描述')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name_plural': '城市',
                'verbose_name': '城市',
            },
        ),
        migrations.CreateModel(
            name='CourseOrg',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='机构名称')),
                ('desc', DjangoUeditor.models.UEditorField(verbose_name='机构描述', default='')),
                ('tag', models.CharField(max_length=10, verbose_name='机构标签', default='全国知名')),
                ('category', models.CharField(max_length=20, verbose_name='机构类别', choices=[('pxjg', '培训机构'), ('gr', '个人'), ('gx', '高校')], default='pxjg')),
                ('click_nums', models.IntegerField(verbose_name='点击数', default=0)),
                ('fav_nums', models.IntegerField(verbose_name='收藏数', default=0)),
                ('image', models.ImageField(upload_to='org/%Y/%m', verbose_name='logo')),
                ('address', models.CharField(max_length=150, verbose_name='机构地址')),
                ('students', models.IntegerField(verbose_name='学习人数', default=0)),
                ('course_nums', models.IntegerField(verbose_name='课程数', default=0)),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
                ('city', models.ForeignKey(to='organization.CityDict', verbose_name='所在城市')),
            ],
            options={
                'verbose_name_plural': '课程机构',
                'verbose_name': '课程机构',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='教师名')),
                ('work_years', models.IntegerField(verbose_name='工作年限', default=0)),
                ('work_company', models.CharField(max_length=50, verbose_name='就职公司')),
                ('work_position', models.CharField(max_length=50, verbose_name='公司职位')),
                ('points', models.CharField(max_length=50, verbose_name='教学特点')),
                ('click_nums', models.IntegerField(verbose_name='点击数', default=0)),
                ('fav_nums', models.IntegerField(verbose_name='收藏数', default=0)),
                ('age', models.IntegerField(verbose_name='年龄', default=18)),
                ('image', models.ImageField(upload_to='teacher/%Y/%m', verbose_name='头像', default='')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
                ('org', models.ForeignKey(to='organization.CourseOrg', verbose_name='所属机构')),
            ],
            options={
                'verbose_name_plural': '教师',
                'verbose_name': '教师',
            },
        ),
    ]
