from django.test import TestCase
from .models import Label


class LabelTestCase(TestCase):
    def setUp(self):
        Label(name='Test label #1').save()
        Label(name='Test label #2').save()

    def testCreate(self):
        self.assertEqual(len(Label.objects.all()), 2)
        self.assertEqual(Label.objects.all()[0].name, 'Test label #1')
        self.assertEqual(Label.objects.all()[1].name, 'Test label #2')

    def testUpdate(self):
        label1 = Label.objects.get(id=1)
        label1.name = 'Test label #1 updated'
        label1.save()
        self.assertEqual(Label.objects.get(id=1).name, 'Test label #1 updated')

    def testDelete(self):
        self.assertEqual(len(Label.objects.all()), 2)
        Label.objects.get(id=1).delete()
        self.assertEqual(len(Label.objects.all()), 1)
        self.assertEqual(Label.objects.all()[0].name, 'Test label #2')
