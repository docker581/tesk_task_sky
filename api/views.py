from django.shortcuts import get_object_or_404

from rest_framework import mixins, viewsets
from rest_framework import response

from data.models import Patient, Case, Document
from .serializers import PatientSerializer, CaseSerializer, DocumentSerializer


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

    # def retrieve(self, request, pk=None):
    #     queryset = Document.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = DocumentSerializer
    #     return response.Response(serializer.data)
