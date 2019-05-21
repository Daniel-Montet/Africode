# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_course_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='times_taken',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
