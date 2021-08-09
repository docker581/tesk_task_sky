from rest_framework import mixins, viewsets
from rest_framework import response
from rest_framework import status

from data.models import Patient, Case, Document, Body
from .serializers import (
    PatientSerializer, 
    CaseSerializer,
    DetailCaseSerializer, 
    DocumentSerializer, 
    DetailDocumentSerializer,
)


class PatientViewSet(
    mixins.RetrieveModelMixin, 
    mixins.CreateModelMixin, 
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()


class CaseViewSet(
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin, 
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = CaseSerializer
    queryset = Case.objects.all()
    filterset_fields = ['patient']
    # если понадобится фильтрация по ФИО пациента, а не по id
    # filterset_fields = ['patient__fio']

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = DetailCaseSerializer(instance)
        return response.Response(serializer.data)


class DocumentViewSet(
    mixins.RetrieveModelMixin, 
    mixins.CreateModelMixin, 
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()
    filter_fields = ['patient', 'case']

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = DetailDocumentSerializer(instance)
        return response.Response(serializer.data)
