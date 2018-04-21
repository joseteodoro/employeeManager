from ..serializers import DepartmentSerializer, EmployeeSerializer
from ..models import Department, Employee
from django.test import TestCase

class SerializerTest(TestCase):
    """ Test module for Department serializer """

    def setUp(self):
        self.hauting = Department(name='hauting')
        self.hauting.save()

    def test_department_serializer(self):
        serializer = DepartmentSerializer(self.hauting)
        serialized = {'pk': 1, 'name': 'hauting'}
        self.assertEqual(serializer.data, serialized)

    def tearDown(self):
        self.hauting.delete()
