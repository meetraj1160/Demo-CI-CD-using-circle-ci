from django.http import JsonResponse
from django.urls import path

def hello(request):
    return JsonResponse({"message": "Hello, CI/CD!"})

urlpatterns = [
    path("hello/", hello),
]
