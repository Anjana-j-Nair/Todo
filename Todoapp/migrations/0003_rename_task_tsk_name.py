# Generated by Django 4.2.6 on 2023-10-09 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Todoapp', '0002_tsk_delete_tasks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tsk',
            old_name='task',
            new_name='name',
        ),
    ]