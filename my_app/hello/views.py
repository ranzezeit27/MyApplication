from django.shortcuts import render, HttpResponse

# Create your views here.
def show(request):
    return HttpResponse('Hello world haha');

def not_so(request):
    return HttpResponse("Not show");