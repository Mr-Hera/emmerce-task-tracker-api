from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Tasks
from .serializers import TasksSerializer

# Create your views here.

@api_view(['GET'])
def endpoints(request):
    data = ['/tasks', 'tasks/<str:pk>/' ]
    return Response(data)

@api_view(['GET'])
def task_list(request):
    tasks = Tasks.objects.all()
    serializer = TasksSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def task_detail(request, pk):
    task = Tasks.objects.get(id=pk)
    serializer = TasksSerializer(task, many=False)
    return Response(serializer.data)