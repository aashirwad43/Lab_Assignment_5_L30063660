from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

# Create your views here.
def hello_api(request):
    if request.method == "GET":
        return JsonResponse({"Message": "Hello World!"})

    else:
        return HttpResponse()