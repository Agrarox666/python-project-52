from django.test import TestCase
from django.urls import reverse
from .models import Label
from ..read_json import get_json_data
from ..users.models import TaskUser


class LabelTestCase(TestCase):
    fixture = ['labels.json', 'users.json']

    def setUp(self):
        user_data = get_json_data(self.fixture[1])['test']
        TaskUser.objects.create_user(**user_data)

        self.create_label = reverse('label_create')
        self.labels_data = get_json_data(self.fixture[0])
        self.client.login(
            username=user_data['username'],
            password=user_data['password']
        )
        self.client.post(self.create_label, self.labels_data['label#1'])

    def testCreate(self):
        self.assertEqual(len(Label.objects.all()), 1)
        self.assertEqual(Label.objects.all()[0].name, 'Testing')

        response = self.client.post(self.create_label, self.labels_data['label#2'])
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(Label.objects.all()), 2)
        self.assertEqual(Label.objects.all()[0].name, 'Testing')
        self.assertEqual(Label.objects.all()[1].name, 'Deploy')

    def testUpdate(self):
        test_label = Label.objects.get(name='Testing')
        response = self.client.post(
            reverse('label_update', args=[test_label.id]),
            self.labels_data['label_update']
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            Label.objects.get(id=test_label.id).name,
            self.labels_data['label_update'].get('name')
        )

    def testDelete(self):
        self.assertEqual(len(Label.objects.all()), 1)
        test_label = Label.objects.get(name='Testing')
        response = self.client.post(
            reverse('label_delete', args=[test_label.id]),
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(Label.objects.all()), 0)
