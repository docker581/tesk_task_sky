from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import PatientViewSet, CaseViewSet, DocumentViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patients')
router.register(r'cases', CaseViewSet, basename='cases')
router.register(r'documents', DocumentViewSet, basename='documents')
urlpatterns = [
    path('', include(router.urls)),
]
