# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0001_initial'),
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfavorite',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='usercourse',
            name='course',
            field=models.ForeignKey(to='courses.Course', verbose_name='课程'),
        ),
        migrations.AddField(
            model_name='usercourse',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='coursecomments',
            name='course',
            field=models.ForeignKey(to='courses.Course', verbose_name='课程'),
        ),
        migrations.AddField(
            model_name='coursecomments',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
    ]
