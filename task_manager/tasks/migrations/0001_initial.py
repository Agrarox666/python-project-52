# Generated by Django 4.2.7 on 2023-12-16 12:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('statuses', '0001_initial'),
        ('labels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(default=None)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='task_author', to=settings.AUTH_USER_MODEL)),
                ('executor', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='task_executor', to=settings.AUTH_USER_MODEL)),
                ('labels', models.ManyToManyField(to='labels.label')),
                ('status', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='task_status', to='statuses.status')),
            ],
        ),
    ]
