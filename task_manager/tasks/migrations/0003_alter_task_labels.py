# Generated by Django 4.2.7 on 2023-12-19 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
        ('tasks', '0002_alter_task_author_alter_task_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='labels',
            field=models.ManyToManyField(blank=True, default=None, to='labels.label'),
        ),
    ]
