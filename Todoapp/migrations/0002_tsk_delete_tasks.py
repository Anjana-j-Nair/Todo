# Generated by Django 4.2.6 on 2023-10-09 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tsk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=250)),
                ('priority', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Tasks',
        ),
    ]
