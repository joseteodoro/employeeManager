from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    url(r'^', include('employee.urls')),
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
]