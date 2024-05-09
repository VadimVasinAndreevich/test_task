from django.db import models


class Customer(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=32)
    surname = models.CharField(verbose_name='Фамилия', max_length=32)
    patronymic = models.CharField(verbose_name='Отчество', max_length=32)
    telephone_number = models.CharField(verbose_name='Номер телефона', max_length=24, blank=True)
    email = models.EmailField(verbose_name='Электронная почта', max_length=50, unique=True)
    password = models.CharField(verbose_name='пароль', max_length=20, unique=True)


class Executor(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=32)
    surname = models.CharField(verbose_name='Фамилия', max_length=32)
    patronymic = models.CharField(verbose_name='Отчество', max_length=32)
    telephone_number = models.CharField(verbose_name='Номер телефона', max_length=24, blank=True)
    experience = models.TextField(verbose_name='Деятельность', blank=True)
    email = models.EmailField(verbose_name='Электронная почта', max_length=50, unique=True)
    password = models.CharField(verbose_name='Пароль', max_length=20, unique=True)
