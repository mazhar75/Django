# This was created by Nihad
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def Conversion(request):
    text=request.GET.get('textfield','default')
    check1 = request.GET.get('lower','off')
    check2 = request.GET.get('upper','off')
    check3 = request.GET.get('space','off')
    
    #print(Check)
    dict = {}
    low=''
    if check1=='on':
        for char in text:
            if 'a'<=char<='z':
                low = low + chr(ord(char)-97+65)
            else: low = low + char    
        dict={'ToLower':''}
    else :
        return HttpResponse('Please on the check button')
    