from django.db import models
from django.contrib.auth.models import User


# Database models for core app


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    hire_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(
        max_length=10, choices=[("Present", "Present"), ("Absent", "Absent")]
    )
    check_in = models.TimeField(null=True, blank=True)
    check_out = models.TimeField(null=True, blank=True)


class Performance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    review_date = models.DateField()
    rating = models.IntegerField()
    notes = models.TextField()
