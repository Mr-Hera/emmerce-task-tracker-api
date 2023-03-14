from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from rest_framework.response import Response
from .models import Tasks
from .serializers import TasksSerializer

# Create your views here.

@api_view(['GET'])
def endpoints(request):
    data = ['/tasks', 'tasks/<str:pk>/' ]
    return Response(data)

@api_view(['GET', 'POST'])
def task_list(request):
    # for GET requests
    if request.method == 'GET':
        tasks = Tasks.objects.all()
        serializer = TasksSerializer(tasks, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        task = Tasks.objects.create(
            title = request.data['title'],
            date = request.data['date'],
        )
        serializer = TasksSerializer(task, many=False)
        return Response(serializer.data)

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