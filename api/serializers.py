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


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Document


class BodySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Body
