from rest_framework import viewsets, filters
from .models import Employee, Attendance, Performance
from .serializers import EmployeeSerializer, AttendanceSerializer, PerformanceSerializer
from rest_framework.permissions import IsAuthenticated
from django.views.generic import TemplateView
import json


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name", "department"]
    ordering_fields = ["hire_date"]


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]


class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
    permission_classes = [IsAuthenticated]


class PerformanceChartView(TemplateView):
    template_name = "chart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data"] = json.dumps(
            {
                emp.name: list(emp.performance_set.values_list("rating", flat=True))
                for emp in Employee.objects.all()
            }
        )
        return context
