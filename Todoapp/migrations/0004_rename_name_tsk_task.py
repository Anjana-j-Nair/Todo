# Generated by Django 4.2.6 on 2023-10-09 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Todoapp', '0003_rename_task_tsk_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tsk',
            old_name='name',
            new_name='task',
        ),
    ]
