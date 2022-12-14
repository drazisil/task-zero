from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("new", views.create, name='new'),
    path('list', views.list, name='list'),
    path('edit/<int:task_id>', views.edit, name='edit'),
]