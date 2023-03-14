from django.urls import path
from . import views

urlpatterns = [
    path('', views.endpoints),
    path('tasks/', views.task_list, name='tasks'),
    path('tasks/<str:pk>/', views.task_detail)
]