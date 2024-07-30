from django.shortcuts import render,HttpResponse

# Create your views here.
def add(request,a,b):
    return HttpResponse(f"the addition of {a} and {b} is : {a+b}")
