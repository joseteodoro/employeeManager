from django.conf.urls import url
from django.urls import include
from rest_framework import routers
from .serializers import DepartmentViewSet, EmployeeViewSet
from . import views

router = routers.DefaultRouter()
router.register(r'employee', EmployeeViewSet)
router.register(r'department', DepartmentViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^employee/$', views.employee_detail, name='employee'),
    url(r'^employee/(?P<pk>[0-9]+)/$', views.employee_detail,name='employee-detail'),
    url(r'^department/$', views.department_detail, name='department'),
    url(r'^department/(?P<pk>[0-9]+)/$', views.department_detail,name='department-detail'),
]