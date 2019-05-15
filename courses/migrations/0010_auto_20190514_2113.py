# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_mulitiplechoicequestion_truefalsequestion'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MulitipleChoiceQuestion',
            new_name='MultipleChoiceQuestion',
        ),
    ]
