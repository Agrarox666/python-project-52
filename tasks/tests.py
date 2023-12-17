from django.test import TestCase

from labels.models import Label
from statuses.models import Status
from users.models import TaskUser
from .models import Task


class TaskTestCase(TestCase):
    def setUp(self):
        user1 = TaskUser(first_name='Igor', last_name='Loskutov', username='agrarox')
        user1.save()
        user2 = TaskUser(first_name='Denis', last_name='Ivanov', username='denchik')
        user2.save()
        status1 = Status(name='Testing')
        status1.save()
        label1 = Label(name='Critical')
        label1.save()

        '''task1 = Task(name='Deployment of 4th project',
                     author=user1,
                     executor=user2,
                     status=status1,
                     description='Description of the deployment.')'''
        task1 = Task(
            name='Deployment of 4th project',
            description='Description of the deployment.')
        task1.author = user1
        task1.executor = user2
        task1.status = status1
        task1.save()

        task1.labels.add(label1)
        task1.save()

    def testCreate(self):
        self.assertEqual(len(Task.objects.all()), 1)
        self.assertEqual(Task.objects.all()[0].name, 'Deployment of 4th project')
        self.assertEqual(Task.objects.all()[0].author.first_name, 'Igor')
        self.assertEqual(Task.objects.all()[0].executor.first_name, 'Denis')
        self.assertEqual(Task.objects.all()[0].labels.all()[0].name, 'Critical')
        self.assertEqual(Task.objects.all()[0].status.name, 'Testing')

    def testUpdate(self):
        task1 = Task.objects.all()[0]
        task1.name = 'Deployment of 4th project updated'
        task1.save()
        self.assertEqual(Task.objects.all()[0].name, 'Deployment of 4th project updated')

    def testDelete(self):
        self.assertEqual(len(Task.objects.all()), 1)
        Task.objects.all()[0].delete()
        self.assertEqual(len(Task.objects.all()), 0)
