from django.test import TestCase
from .models import Status


class StatusTestCase(TestCase):
    def setUp(self):
        Status(name='Test status #1').save()
        Status(name='Test status #2').save()

    def testCreate(self):
        self.assertEqual(len(Status.objects.all()), 2)
        self.assertEqual(Status.objects.all()[0].name, 'Test status #1')
        self.assertEqual(Status.objects.all()[1].name, 'Test status #2')

    def testUpdate(self):
        label1 = Status.objects.get(id=1)
        label1.name = 'Test status #1 updated'
        label1.save()
        self.assertEqual(Status.objects.get(id=1).name, 'Test status #1 updated')

    def testDelete(self):
        self.assertEqual(len(Status.objects.all()), 2)
        Status.objects.get(id=1).delete()
        self.assertEqual(len(Status.objects.all()), 1)
        self.assertEqual(Status.objects.all()[0].name, 'Test status #2')
