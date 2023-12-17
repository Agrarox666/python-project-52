from django.test import TestCase
from .models import TaskUser


class TaskUserTestCase(TestCase):
    def setUp(self):
        TaskUser(first_name='Igor', last_name='Loskutov', username='agrarox').save()
        TaskUser(first_name='Denis', last_name='Ivanov', username='denchik').save()

    def testCreate(self):
        self.assertEqual(len(TaskUser.objects.all()), 2)

        self.assertEqual(TaskUser.objects.all()[0].first_name, 'Igor')
        self.assertEqual(TaskUser.objects.all()[0].last_name, 'Loskutov')
        self.assertEqual(TaskUser.objects.get(id=1).username, 'agrarox')
        self.assertEqual(TaskUser.objects.get(id=2).first_name, 'Denis')

    def testUpdate(self):
        user1 = TaskUser.objects.get(id=1)
        user1.username = 'updated_username'
        user1.save()
        self.assertEqual(TaskUser.objects.get(id=1).username, 'updated_username')

    def testDelete(self):
        self.assertEqual(len(TaskUser.objects.all()), 2)
        TaskUser.objects.get(first_name='Igor').delete()
        self.assertEqual(len(TaskUser.objects.all()), 1)
        self.assertEqual(TaskUser.objects.all()[0].username, 'denchik')
