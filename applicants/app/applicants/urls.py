from django.contrib import admin
from django.urls import path
from .views import UsersView

urlpatterns = [
    path('register/', UsersView.as_view(), name='users_view'),
]
