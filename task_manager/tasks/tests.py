from django import test
from django.test import TestCase
from django.urls import reverse

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.users.models import TaskUser
from .models import Task
from ..read_json import get_json_data


@test.modify_settings(MIDDLEWARE={'remove': [
    'rollbar.contrib.django.middleware.RollbarNotifierMiddleware',
]})
class TaskTestCase(TestCase):
    fixture = ['tasks.json', 'users.json', 'labels.json', 'statuses.json']

    def setUp(self):
        self.task_data = get_json_data(self.fixture[0])
        self.user_data = get_json_data(self.fixture[1])
        self.label_data = get_json_data(self.fixture[2])
        self.statuses_data = get_json_data(self.fixture[3])

        self.user = TaskUser.objects.create_user(**self.user_data['test'])
        self.user_executor = TaskUser(**self.user_data['task_user1'])
        self.status = Status(**self.statuses_data['task_status'])
        self.label = Label(**self.label_data['task_label'])
        self.user_executor.save(), self.label.save(), self.status.save()

        self.client.force_login(self.user)

        task1 = Task(
            name=self.task_data['test']['name'],
            description=self.task_data['test']['description'],
            executor=self.user_executor,
            author=self.user,
            status=self.status,
        )
        task1.save()

    def testCreate(self):
        self.assertEqual(
            len(Task.objects.all()),
            1
        )
        test_task = {
            "name": self.task_data['test#2']['name'],
            "description": self.task_data['test#2']['description'],
            "status": self.status.pk,
            "executor": self.user.pk,
            "labels": self.label.pk,
        }
        response = self.client.post(
            reverse('task_create'),
            test_task
        )

        self.assertEqual(
            response.status_code,
            302
        )
        self.assertEqual(
            len(Task.objects.all()),
            2
        )

    def testUpdate(self):
        test_task = Task.objects.all()[0]
        status = Status(**self.statuses_data.get('status_update'))
        label = Label(**self.label_data.get('label_update'))
        status.save(), label.save()
        update_task_data = {
            'name': test_task.name,
            'description': test_task.description,
            'status': status.pk,
            'executor': self.user_executor.pk,
            'labels': label.pk
        }
        response = self.client.post(
            reverse('task_update', args=[test_task.id]),
            update_task_data
        )
        self.assertEqual(
            response.status_code,
            302
        )
        self.assertEqual(
            test_task.executor.full_name,
            self.user_executor.full_name
        )

    def testDelete(self):
        test_task = Task.objects.all()[0]
        self.client.post(
            reverse('task_delete', args=[test_task.id])
        )
        self.assertEqual(
            len(Task.objects.all()),
            0
        )
