from django.urls import path
from . import views
from .views import RegisterAPI, LoginAPI
from knox import views as knox_views

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),

    path('', views.endpoints),
    path('tasks/', views.task_list, name='tasks'),
    path('tasks/<str:pk>/', views.task_detail)

]