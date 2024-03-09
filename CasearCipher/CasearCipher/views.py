from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def interface(request):
    text=request.GET.get('textfield','default')
    check = request.GET.get('Doit','off')
    return HttpResponse(text)