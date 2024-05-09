from django.urls import path
from .views import main_index, add_customer, add_executor, login_customer, login_executor, logout_user


urlpatterns = [
    path('', main_index, name='main_index'),
    path('add_customer', add_customer, name='add_customer'),
    path('add_executor', add_executor, name='add_executor'),
    path('login_customer', login_customer, name='login_customer'),
    path('login_executor', login_executor, name='login_executor'),
    path('logout_user', logout_user, name='logout_user'),
]
