from django.test import TestCase
from django.urls import reverse

from .models import TaskUser
from ..read_json import get_json_data


class TaskUserTestCase(TestCase):
    fixture = 'users.json'

    def setUp(self):
        self.user_data = get_json_data(self.fixture)
        self.client.post(
            reverse('user_create'),
            self.user_data['user#1']
        )
        self.client.login(
            username=self.user_data['user#1']['username'],
            password=self.user_data['user#1']['password1']
        )

    def testCreate(self):
        self.assertEqual(len(TaskUser.objects.all()), 1)
        test_user = self.user_data['user#2']
        response = self.client.post(
            reverse('user_create'),
            test_user
        )
        self.assertEqual(
            response.status_code,
            302
        )
        self.assertEqual(
            len(TaskUser.objects.all()),
            2
        )

    def testUpdate(self):
        test_user = TaskUser.objects.get(first_name=self.user_data['user#1']['first_name'])
        update_user = self.user_data['user#2']
        response = self.client.post(
            reverse('user_update', args=[test_user.id]),
            update_user
        )
        self.assertEqual(
            response.status_code,
            302
        )
        self.assertEqual(
            TaskUser.objects.get(id=test_user.id).first_name,
            self.user_data['user#2'].get('first_name')
        )

    def testDelete(self):
        test_user = TaskUser.objects.all()[0]
        self.assertEqual(
            len(TaskUser.objects.all()),
            1
        )
        response = self.client.post(
            reverse('user_delete', args=[test_user.id])
        )
        self.assertEqual(
            response.status_code,
            302
        )
        self.assertEqual(
            len(TaskUser.objects.all()),
            0
        )
