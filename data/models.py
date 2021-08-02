from django.db import models
from django.utils.translation import gettext_lazy as _

import jsonfield


class Patient(models.Model):
    class PatientGender(models.TextChoices):
        MALE = 'М', _('Мужской')
        FEMALE = 'Ж', _('Женский')

    fio = models.CharField(max_length=100, verbose_name="ФИО")
    birth_date = models.DateField(verbose_name="Дата рождения")
    gender = models.CharField(
        max_length=50, 
        choices=PatientGender.choices,
        verbose_name="Пол",
    )

    class Meta:
        verbose_name = "Пациент"
        verbose_name_plural = "Пациенты"

    def __str__(self):
        return f"Пациент {self.fio}"


class Case(models.Model):
    class CaseResult(models.TextChoices):
        POSITIVE = 'П', _('Положительный')
        NEGATIVE = 'О', _('Отрицательный')

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="cases",
        verbose_name="пациент",
    )
    date_begin = models.DateField(verbose_name="Дата начала")
    date_end = models.DateField(
        blank=True, 
        null=True, 
        verbose_name="Дата окончания",
    )
    result = models.CharField(
        max_length=50, 
        choices=CaseResult.choices,
        blank=True, 
        null=True, 
        verbose_name="Исход",
    )

    class Meta:
        verbose_name = "Случай лечения"
        verbose_name_plural = "Случаи лечения"

    def __str__(self):
        return f"Лечение пациента {self.patient}"


class Document(models.Model):
    patient = models.ForeignKey(
        Patient, 
        on_delete=models.CASCADE, 
        verbose_name="Пациент",
    )
    case = models.ForeignKey(
        Case, 
        on_delete=models.SET_NULL,
        blank=True, 
        null=True, 
        verbose_name="Случай лечения",
    )
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    date = models.DateField(verbose_name="Дата документа")

    class Meta:
        verbose_name = "Медицинский документ"
        verbose_name_plural = "Медицинские документы"

    def __str__(self):
        return f"Документ {self.title}"


class Body(models.Model):
    document = models.OneToOneField(
        Document,
        on_delete=models.CASCADE,
        verbose_name="Документ",   
    )    
    content = jsonfield.JSONField()
