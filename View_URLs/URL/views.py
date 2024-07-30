from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")
def hello(request,name):
    return HttpResponse(f"Hello,\n welcome back {name}")

