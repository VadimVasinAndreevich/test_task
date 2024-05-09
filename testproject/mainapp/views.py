from .models import Customer, Executor
from .forms import CustomerForm, ExecutorForm, UserLoginForm
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.core.files.storage import FileSystemStorage
import os


def main_index(request):
    """Главная страница"""
    message = 'Добро пожаловать'
    name_user = request.session.get('name_user', '')
    return render(request, 'mainapp/index.html', {'name_user': name_user, 'message': message})


def add_customer(request):
    """Создание учётной записи заказчика"""
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid() and request.POST['password'] == request.POST['repeat_password']:
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            patronymic = form.cleaned_data['patronymic']
            telephone_number = form.cleaned_data['telephone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            customer = Customer(name=name, surname=surname, patronymic=patronymic, telephone_number=telephone_number,
                                email=email, password=password)
            customer.save()
            message = 'Пользователь сохранён, теперь можете авторизоваться и разместить объявление'
            return render(request, 'mainapp/index.html', {'message': message})
    else:
        form = CustomerForm()
        message = 'Заполните форму'
    return render(request, 'mainapp/form.html', {'form': form, 'message': message})


def add_executor(request):
    """Создание учётной записи исполнителя"""
    if request.method == 'POST':
        form = ExecutorForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid() and request.POST['password'] == request.POST['repeat_password']:
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            patronymic = form.cleaned_data['patronymic']
            telephone_number = form.cleaned_data['telephone_number']
            experience = form.cleaned_data['experience']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            executor = Executor(name=name, surname=surname, patronymic=patronymic, telephone_number=telephone_number,
                                experience=experience, email=email, password=password)
            executor.save()
            message = 'Пользователь сохранён, теперь можете авторизоваться и разместить объявление'
            return render(request, 'mainapp/index.html', {'message': message})
    else:
        form = ExecutorForm()
        message = 'Заполните форму'
    return render(request, 'mainapp/form.html', {'form': form, 'message': message})


def login_customer(request):
    """Авторизация заказчика"""
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        customer = Customer.objects.filter(email=request.POST['email'], password=request.POST['password']).first()
        message = 'Ошибка в данных, неверно введены: адрес электронной почты или пароль'
        if customer is not None:
            request.session['name_user'] = customer.name
            name_user = request.session['name_user']
            message = 'Вы вошли в систему'
            return render(request, 'mainapp/index.html', {'name_user': name_user, 'message': message})
    else:
        form = UserLoginForm()
        message = 'Введите адрес электронной почты и пароль для авторизации'
    return render(request, 'mainapp/form.html', {'form': form, 'message': message})


def login_executor(request):
    """Авторизация сполнителя"""
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        executor = Executor.objects.filter(email=request.POST['email'], password=request.POST['password']).first()
        message = 'Ошибка в данных, неверно введены: адрес электронной почты или пароль'
        if executor is not None:
            request.session['name_user'] = executor.name
            name_user = request.session['name_user']
            message = 'Вы вошли в систему'
            return render(request, 'mainapp/index.html', {'name_user': name_user, 'message': message})
    else:
        form = UserLoginForm()
        message = 'Введите адрес электронной почты и пароль для авторизации'
    return render(request, 'mainapp/form.html', {'form': form, 'message': message})


def logout_user(request):
    """Выход из учётной записи"""
    del request.session['name_user']
    message = 'Вы вышли из учётной записи'
    return render(request, 'mainapp/index.html', {'message': message})
