# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import datetime
import django.core.validators
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', default=False, verbose_name='superuser status')),
                ('username', models.CharField(validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], verbose_name='username', error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, unique=True)),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(help_text='Designates whether the user can log into this admin site.', default=False, verbose_name='staff status')),
                ('is_active', models.BooleanField(help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', default=True, verbose_name='active')),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('nick_name', models.CharField(max_length=50, verbose_name='昵称', default='')),
                ('birday', models.DateField(null=True, verbose_name='生日', blank=True)),
                ('gender', models.CharField(max_length=6, choices=[('male', '男'), ('female', '女')], default='female')),
                ('address', models.CharField(max_length=100, default='')),
                ('mobile', models.CharField(max_length=11, null=True, blank=True)),
                ('image', models.ImageField(upload_to='image/%Y/%m', default='image/default.png')),
                ('groups', models.ManyToManyField(verbose_name='groups', to='auth.Group', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_query_name='user', related_name='user_set', blank=True)),
                ('user_permissions', models.ManyToManyField(verbose_name='user permissions', to='auth.Permission', help_text='Specific permissions for this user.', related_query_name='user', related_name='user_set', blank=True)),
            ],
            options={
                'verbose_name_plural': '用户信息',
                'verbose_name': '用户信息',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('image', models.ImageField(upload_to='banner/%Y/%m', verbose_name='轮播图')),
                ('url', models.URLField(verbose_name='访问地址')),
                ('index', models.IntegerField(verbose_name='顺序', default=100)),
                ('add_time', models.DateTimeField(verbose_name='添加时间', default=datetime.datetime.now)),
            ],
            options={
                'verbose_name_plural': '轮播图',
                'verbose_name': '轮播图',
            },
        ),
        migrations.CreateModel(
            name='EmailVerifyRecord',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='验证码')),
                ('email', models.EmailField(max_length=50, verbose_name='邮箱')),
                ('send_type', models.CharField(max_length=30, verbose_name='验证码类型', choices=[('register', '注册'), ('forget', '找回密码'), ('update_email', '修改邮箱')])),
                ('send_time', models.DateTimeField(verbose_name='发送时间', default=datetime.datetime.now)),
            ],
            options={
                'verbose_name_plural': '邮箱验证码',
                'verbose_name': '邮箱验证码',
            },
        ),
    ]
