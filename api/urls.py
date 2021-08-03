from django.urls import path
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import PatientViewSet, CaseViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patients')
router.register(r'cases', CaseViewSet, basename='cases')
urlpatterns = [
    path('', include(router.urls)),
]