from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return "Department {}".format(self.name)


class Employee(models.Model):
    name = models.CharField(max_length=200, verbose_name="Employee's name")
    email = models.EmailField(verbose_name="Email")
    department = models.ForeignKey(Department, on_delete=models.PROTECT, verbose_name="Department")

    def by_department(self, department):
        return Employee.objects.filter(department__name=department)

    def by_name(self, name):
        return Employee.objects.filter(*name)

    def __str__(self):
        return "{} of {}".format(self.name, self.department)