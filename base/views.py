from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from rest_framework.response import Response
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from .models import Tasks
from .serializers import TasksSerializer

# Display of available endpoints

@api_view(['GET'])
def endpoints(request):
    data = ['register/', 'login/', 'logout/', 'tasks/', 'tasks/<str:pk>/'  ]
    return Response(data)

# CRUD functionality

@api_view(['GET', 'POST'])
def task_list(request):
    # GET all tasks
    if request.method == 'GET':
        tasks = Tasks.objects.all()
        serializer = TasksSerializer(tasks, many=True)
        return Response(serializer.data)

    # CREATE a task
    if request.method == 'POST':
        task = Tasks.objects.create(
            title = request.data['title'],
            date = request.data['date'],
        )
        serializer = TasksSerializer(task, many=False)
        return Response(serializer.data)

# UPDATING individual task

@api_view(['GET', 'PUT', 'DELETE'])
def task_detail(request, pk):
    task = Tasks.objects.get(id=pk)

    if request.method == 'GET':
        serializer = TasksSerializer(task, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        task.title = request.data['title']
        task.date = request.data['date']

        task.save()

        serializer = TasksSerializer(task, many=False)
        return Response(serializer.data)

    if request.method == 'DELETE':
        task.delete()
        return Response('Deleted Successfully!')

# Register API

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

# Login API

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)