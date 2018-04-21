import json
from django.urls import reverse

from rest_framework.test import APITestCase


from django.test import TestCase
from ..models import Department, Employee


class EmployeeTest(TestCase):
    """ Test module for Employee model """

    def setUp(self):
        self.hauting = Department(name='hauting')
        self.hauting.save()

        self.casper = Employee(name='Casper', email='casper@hotmail.com', department=self.hauting)
        self.casper.save()

    def test_casper(self):
        casper = Employee.objects.get(name='Casper')
        self.assertEqual(casper.name, 'Casper')
        self.assertEqual(casper.department.name, 'hauting')

    def tearDown(self):
        self.casper.delete()
        self.hauting.delete()


class EmployeeListCreateAPIViewTest(APITestCase):

    def setUp(self):
        self.client.login(username="test", password="test")

    def test_emptyList(self):
        url = reverse("employee")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual([], json.loads(response.content))

    def test_nonEmptyList(self):
        hauting = Department(name='hauting')
        hauting.save()

        casper = Employee(name='Casper', email='casper@hotmail.com', department=hauting)
        casper.save()

        url = reverse("employee")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        expected_json = [{'department': 'http://testserver/department/1/',
                         'email': 'casper@hotmail.com',
                         'name': 'Casper'}]
        self.assertEqual(expected_json, json.loads(response.content))

        casper.delete()
        hauting.delete()

    def test_unauthorized_request(self):
        url = reverse("department")
        response = self.client.post(url, {"name": "hr"})
        self.assertEqual(403, response.status_code)
