from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return "{} of {}".format(self.name, self.department)