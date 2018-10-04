# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20160128_1628'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='documents',
            options={'verbose_name': 'Document', 'verbose_name_plural': 'Documents'},
        ),
        migrations.AlterModelOptions(
            name='teammembers',
            options={'verbose_name': 'Team Member', 'verbose_name_plural': 'Team Members'},
        ),
        migrations.RenameField(
            model_name='documents',
            old_name='type',
            new_name='doc_type',
        ),
        migrations.RenameField(
            model_name='documenttype',
            old_name='type',
            new_name='type_name',
        ),
        migrations.AlterField(
            model_name='project',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='projects.ClientList', null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='projects.ProjectManager', null=True),
        ),
    ]
