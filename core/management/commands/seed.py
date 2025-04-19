# Generating synthetic data using faker library
from faker import Faker
from core.models import Employee, Attendance, Performance
from django.core.management.base import BaseCommand
import random
from datetime import timedelta, date

fake = Faker()


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for _ in range(5):
            emp = Employee.objects.create(
                name=fake.name(),
                email=fake.unique.email(),
                position=random.choice(["Developer", "Manager", "Analyst"]),
                department=random.choice(["HR", "Tech", "Finance"]),
                hire_date=fake.date_between(start_date="-2y", end_date="today"),
            )
            for i in range(10):
                Attendance.objects.create(
                    employee=emp,
                    date=fake.date_this_year(),
                    status=random.choice(["Present", "Absent"]),
                    check_in=fake.time_object(),
                    check_out=fake.time_object(),
                )
                Performance.objects.create(
                    employee=emp,
                    review_date=fake.date_this_year(),
                    rating=random.randint(1, 5),
                    notes=fake.sentence(),
                )
