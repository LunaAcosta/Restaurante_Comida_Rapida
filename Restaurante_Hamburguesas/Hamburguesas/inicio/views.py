from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')

def acercade(request):
    return render(request,'acerca.html')

def base(request):
    return render(request, 'base.html')

def secion(request):
    return render(request, 'secion.html')




