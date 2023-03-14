from .views import RegisterAPI
from django.urls import path
from . import views

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('', views.endpoints),
    path('tasks/', views.task_list, name='tasks'),
    path('tasks/<str:pk>/', views.task_detail)

]