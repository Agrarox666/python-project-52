from django.test import TestCase
from django.urls import reverse

from .models import Status
from ..read_json import get_json_data
from ..users.models import TaskUser


class StatusTestCase(TestCase):
    fixture = ['statuses.json', 'users.json']

    def setUp(self):
        user_data = get_json_data(self.fixture[1])['test']
        TaskUser.objects.create_user(**user_data)

        self.create_status = reverse('status_create')
        self.statuses_data = get_json_data(self.fixture[0])
        self.client.login(
            username=user_data['username'],
            password=user_data['password']
        )
        self.client.post(self.create_status, self.statuses_data['status#1'])

    def testCreate(self):
        self.assertEqual(len(Status.objects.all()), 1)
        self.assertEqual(Status.objects.all()[0].name, 'Done')

        response = self.client.post(self.create_status, self.statuses_data['status#2'])
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(Status.objects.all()), 2)
        self.assertEqual(Status.objects.all()[0].name, 'Done')
        self.assertEqual(Status.objects.all()[1].name, 'In process')

    def testUpdate(self):
        test_status = Status.objects.get(name='Done')
        response = self.client.post(
            reverse('status_update', args=[test_status.id]),
            self.statuses_data['status_update']
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            Status.objects.get(id=test_status.id).name,
            self.statuses_data['status_update'].get('name')
        )

    def testDelete(self):
        self.assertEqual(len(Status.objects.all()), 1)
        test_status = Status.objects.get(name='Done')
        response = self.client.post(
            reverse('status_delete', args=[test_status.id]),
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(Status.objects.all()), 0)
