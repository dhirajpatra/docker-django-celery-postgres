from django.test import TestCase
from celery import Celery
from tasks import sample_tasks
from unittest.mock import patch, call
from django.urls import reverse
from django.test import Client
import json


class YourAppTestCase(TestCase):
    #  Set up your test case here
    def setUp(self):
        # Any setup code needed before each test method
        pass

    def test_home(self):
        client = Client()
        url = reverse("home")
        response = client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_task(self):
        self.assertTrue(sample_tasks.create_task.run(1))
        self.assertTrue(sample_tasks.create_task.run(2))
        self.assertTrue(sample_tasks.create_task.run(3))

    @patch('tasks.sample_tasks.create_task.run')
    def test_mock_task(self, mock_run):
        self.assertTrue(sample_tasks.create_task.run(1))
        mock_run.assert_called_once_with(1)

        self.assertTrue(sample_tasks.create_task.run(2))
        self.assertEqual(mock_run.call_count, 2)

        self.assertTrue(sample_tasks.create_task.run(3))
        self.assertEqual(mock_run.call_count, 3)

    def test_task_status(self):
        client = Client()
        response = client.post(reverse("run_task"), {"type": 0})
        content = json.loads(response.content)
        task_id = content["task_id"]
        self.assertEqual(response.status_code, 202)
        self.assertTrue(task_id)

        response = client.get(reverse("get_status", args=[task_id]))
        content = json.loads(response.content)
        self.assertEqual(
            content, {"task_id": task_id, "task_status": "PENDING", "task_result": None})
        self.assertEqual(response.status_code, 200)

        while content["task_status"] == "PENDING":
            response = client.get(reverse("get_status", args=[task_id]))
            content = json.loads(response.content)

        self.assertEqual(
            content, {"task_id": task_id, "task_status": "SUCCESS", "task_result": True})


# Add more test cases as needed for your Django, Celery, PostgreSQL application
