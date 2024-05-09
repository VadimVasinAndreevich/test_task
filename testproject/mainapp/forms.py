import datetime

from django import forms
from .models import Customer, Executor
from django.contrib.auth.forms import PasswordChangeForm


class CustomerForm(forms.Form):
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                      'placeholder': 'Имя'}))
    surname = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                         'placeholder': 'Фамилия'}))
    patronymic = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                'placeholder': 'Отчество'}))
    telephone_number = forms.CharField(label='Контактный номер', max_length=20,
                                       widget=forms.TextInput(attrs={'class': 'form-control',
                                                                     'placeholder': 'Контактный номер'}))
    email = forms.EmailField(label='Почта',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'user@mail.ru'}))
    password = forms.CharField(label='Пароль', min_length=8, max_length=50,
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                          'placeholder': 'Пароль'}))
    repeat_password = forms.CharField(label='Повтор пароля', min_length=8, max_length=50, widget=forms.PasswordInput(
        attrs={'placeholder': 'Повтор пароля'},))


class ExecutorForm(forms.Form):
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                      'placeholder': 'Имя'}))
    surname = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                         'placeholder': 'Фамилия'}))
    patronymic = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                'placeholder': 'Отчество'}))
    telephone_number = forms.CharField(label='Контактный номер', max_length=20,
                                       widget=forms.TextInput(attrs={'class': 'form-control',
                                                                     'placeholder': 'Контактный номер'}))
    experience = forms.CharField(label='Описание', widget=forms.Textarea(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Почта',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'user@mail.ru'}))
    password = forms.CharField(label='Пароль', min_length=8, max_length=50,
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                          'placeholder': 'Пароль'}))
    repeat_password = forms.CharField(label='Повтор пароля', min_length=8, max_length=50, widget=forms.PasswordInput(
        attrs={'placeholder': 'Повтор пароля'},))


class UserLoginForm(forms.Form):
    email = forms.EmailField(label='Почта',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'user@mail.ru'}))
    password = forms.CharField(label='Пароль', min_length=8, max_length=50,
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                        'placeholder': 'Введите пароль'}))