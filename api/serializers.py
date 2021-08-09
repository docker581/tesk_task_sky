from rest_framework import serializers

from data.models import Patient, Case, Document, Body


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'      


class CaseSerializer(serializers.ModelSerializer):
    # если понадобится выдача ФИО пациента вместо id
    # patient = serializers.ReadOnlyField(source='patient.fio')     

    class Meta:
        model = Case
        fields = ['id', 'patient', 'date_begin', 'date_end', 'result']       


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
        model = Document
        fields = '__all__'       


class DetailDocumentSerializer(serializers.ModelSerializer):
    body = serializers.SerializerMethodField()

    def get_body(self, object):  # получение тела документа
        body = Body.objects.get(document=object).__dict__
        return body['content']

    class Meta:
        model = Document
        fields = ['id', 'body', 'patient', 'case', 'title', 'date']     
