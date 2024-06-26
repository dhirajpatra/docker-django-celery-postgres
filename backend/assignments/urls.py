from django.urls import re_path
from rest_framework.routers import DefaultRouter
from assignments.views import AssignmentViewSet


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'assignments', AssignmentViewSet, basename="assignments")
assignments_urlpatterns = router.urls
