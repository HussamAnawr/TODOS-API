from django.test import TestCase
from ..models import Todo
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

class TodoModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(
            title='First Todo',
            body='A body of text here'
        )
    def test_model_content(self):
        self.assertEqual(self.todo.title, 'First Todo')
        self.assertEqual(self.todo.body, 'A body of text here')
        self.assertEqual(str(self.todo), 'First Todo')

    def test_api_listview(self):
        res = self.client.get(reverse('todos:todo_list'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(res, self.todo)

    def test_api_detailview(self):
        res = self.client.get(reverse('todos:todo_detail', kwargs={'pk':self.todo.id}), format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertContains(res, 'First Todo')