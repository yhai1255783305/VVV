# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='课程名')),
                ('desc', models.CharField(max_length=300, verbose_name='课程描述')),
                ('detail', DjangoUeditor.models.UEditorField(verbose_name='课程详情', default='')),
                ('is_banner', models.BooleanField(default=False, verbose_name='是否轮播')),
                ('degree', models.CharField(max_length=2, verbose_name='难度', choices=[('cj', '初级'), ('zj', '中级'), ('gj', '高级')])),
                ('learn_times', models.IntegerField(verbose_name='学习时长(分钟数)', default=0)),
                ('students', models.IntegerField(verbose_name='学习人数', default=0)),
                ('fav_nums', models.IntegerField(verbose_name='收藏人数', default=0)),
                ('image', models.ImageField(upload_to='courses/%Y/%m', verbose_name='封面图')),
                ('click_nums', models.IntegerField(verbose_name='点击数', default=0)),
                ('category', models.CharField(max_length=20, verbose_name='课程类别', default='后端开发')),
                ('tag', models.CharField(max_length=10, verbose_name='课程标签', default='')),
                ('youneed_know', models.CharField(max_length=300, verbose_name='课程须知', default='')),
                ('teacher_tell', models.CharField(max_length=300, verbose_name='老师告诉你', default='')),
                ('add_time', models.DateTimeField(verbose_name='添加时间', default=datetime.datetime.now)),
                ('course_org', models.ForeignKey(null=True, verbose_name='课程机构', to='organization.CourseOrg', blank=True)),
                ('teacher', models.ForeignKey(null=True, verbose_name='讲师', to='organization.Teacher', blank=True)),
            ],
            options={
                'verbose_name_plural': '课程',
                'verbose_name': '课程',
            },
        ),
        migrations.CreateModel(
            name='CourseResource',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('download', models.FileField(upload_to='course/resource/%Y/%m', verbose_name='资源文件')),
                ('add_time', models.DateTimeField(verbose_name='添加时间', default=datetime.datetime.now)),
                ('course', models.ForeignKey(to='courses.Course', verbose_name='课程')),
            ],
            options={
                'verbose_name_plural': '课程资源',
                'verbose_name': '课程资源',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='章节名')),
                ('learn_times', models.IntegerField(verbose_name='学习时长(分钟数)', default=0)),
                ('add_time', models.DateTimeField(verbose_name='添加时间', default=datetime.datetime.now)),
                ('course', models.ForeignKey(to='courses.Course', verbose_name='课程')),
            ],
            options={
                'verbose_name_plural': '章节',
                'verbose_name': '章节',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='视频名')),
                ('learn_times', models.IntegerField(verbose_name='学习时长(分钟数)', default=0)),
                ('url', models.CharField(max_length=200, verbose_name='访问地址', default='')),
                ('add_time', models.DateTimeField(verbose_name='添加时间', default=datetime.datetime.now)),
                ('lesson', models.ForeignKey(to='courses.Lesson', verbose_name='章节')),
            ],
            options={
                'verbose_name_plural': '视频',
                'verbose_name': '视频',
            },
        ),
        migrations.CreateModel(
            name='BannerCourse',
            fields=[
            ],
            options={
                'verbose_name_plural': '轮播课程',
                'verbose_name': '轮播课程',
                'proxy': True,
            },
            bases=('courses.course',),
        ),
    ]
