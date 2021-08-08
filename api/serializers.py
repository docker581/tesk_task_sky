from rest_framework import serializers

from data.models import Patient, Case, Document, Body


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Patient


class CaseSerializer(serializers.ModelSerializer):
    # если понадобится выдача ФИО пациента вместо id
    # patient = serializers.ReadOnlyField(source='patient.fio')     

    class Meta:
        fields = ['id', 'patient', 'date_begin', 'date_end', 'result']
        model = Case


class DetailCaseSerializer(serializers.ModelSerializer):
    docs = serializers.SerializerMethodField()

    def get_docs(self, object):  # массив док-ов, связанных со случаем
        docs = Document.objects.filter(case=object).values()
        return docs
        
    class Meta:
        fields = ['id', 'docs', 'patient', 'date_begin', 'date_end', 'result']
        model = Case


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Document


class DetailDocumentSerializer(serializers.ModelSerializer):
    # body = serializers.SerializerMethodField()

    # def get_body(self, object):  # получение тела документа
    #     body = Body.objects.get(document=object).__dict__
    #     return body['content']

    class Meta:
        fields = ['id', 'body', 'patient', 'case', 'title', 'date']
        model = Document
