from rest_framework import permissions, serializers, viewsets
from .models import Department, Employee


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ('name', 'email', 'department')


class EmployeeViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    class Meta:
        model = Department
        fields = ['pk','name']


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
