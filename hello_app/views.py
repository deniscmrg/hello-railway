from django.shortcuts import render
from django.http import JsonResponse

def hello_view(request):
    return JsonResponse({"mensagem": "Hello, Denis!"})

