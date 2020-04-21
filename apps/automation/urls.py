# https://www.javatpoint.com/django-crud-example

from django.urls import path
from . import views

app_name = 'automation_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('edit/<int:automation_id>/', views.edit, name='edit'),
    path('delete/<int:automation_id>/', views.delete, name='delete'),
]
