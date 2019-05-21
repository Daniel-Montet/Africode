# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_course_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='subject',
            field=models.CharField(max_length=100, default=''),
        ),
    ]
