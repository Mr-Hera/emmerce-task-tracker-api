from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def endpoints(request):
    data = ['/tasks', 'tasks/<str:pk>/' ]
    return Response(data)

@api_view(['GET'])
def task_list(request):
    data = ['Drifting Event @KICC', 'Doctor appointment' ]
    return Response(data)

@api_view(['GET'])
def task_detail(request, pk):
    data = pk
    return Response(data)