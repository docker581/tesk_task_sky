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
    filterset_fields = ['patient']
    # если понадобится фильтрация по ФИО пациента, а не по id
    # filterset_fields = ['patient__fio']

    # def retrieve(self, request, pk=None):
    #     serializer = DocumentSerializer(many=True)
    #     return response.Response(serializer.data)


class DocumentViewSet(
    mixins.RetrieveModelMixin, 
    mixins.CreateModelMixin, 
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()
    filter_fields = ['patient', 'case']
