from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    EmployeeViewSet,
    AttendanceViewSet,
    PerformanceViewSet,
    PerformanceChartView,
)

router = DefaultRouter()
router.register(r"employees", EmployeeViewSet)
router.register(r"attendance", AttendanceViewSet)
router.register(r"performance", PerformanceViewSet)

urlpatterns = [
    path("", include(router.urls)),  # API endpoints
    path("chart/", PerformanceChartView.as_view(), name="chart"),  # Chart page
]
