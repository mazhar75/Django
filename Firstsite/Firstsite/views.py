# This was created by Nihad
from django.http import HttpResponse

def index(requset):
    return HttpResponse('Hello, This is Mazharul')

def about(request):
    return HttpResponse('About Him!')