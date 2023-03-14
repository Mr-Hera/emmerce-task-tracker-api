from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def endpoints(request):
    data = ['/tasks', 'tasks/<str:pk>/' ]
    return JsonResponse(data, safe=False)

def task_list(request):
    data = ['Drifting Event @KICC', 'Doctor appointment' ]
    return JsonResponse(data, safe=False)

def task_detail(request, pk):
    data = pk
    return JsonResponse(data, safe=False)