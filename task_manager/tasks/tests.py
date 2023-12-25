from django.test import TestCase
from django.urls import reverse

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.users.models import TaskUser
from .models import Task
from ..read_json import get_json_data


class TaskTestCase(TestCase):
    fixture = ['tasks.json', 'users.json', 'labels.json', 'statuses.json']

    def setUp(self):
        self.user_data = get_json_data(self.fixture[1])
        self.label_data = get_json_data(self.fixture[2])
        self.statuses_data = get_json_data(self.fixture[3])

        self.user = TaskUser(**self.user_data['test'])
        self.user_executor = TaskUser(**self.user_data['task_user1'])
        self.status = Status(**self.statuses_data['task_status'])
        self.label = Label(**self.label_data['task_label'])
        self.user.save(), self.user_executor.save(), self.label.save(), self.status.save()

        self.client.login(
            username=self.user.username,
            password=self.user.password
        )
        self.create_task = reverse('task_create')

        task1 = Task(
            name='Test task',
            description='Task description',
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
        status = Status(**get_json_data(self.fixture[3]).get('status_update'))
        status.save()
        test_task = {
            "name": "Test task #2",
            "description": "Simple description",
            "status": self.status.pk,
            "executor": self.user.pk,
            "labels": self.label.pk
        }
        response = self.client.post(
            reverse('task_create'),
            data=test_task
        )

        self.assertEqual(
            response.status_code,
            302
        )
        '''self.assertEqual(
            len(Task.objects.all()),
            2
        )'''

    def testUpdate(self):
        pass

    def testDelete(self):
        pass
