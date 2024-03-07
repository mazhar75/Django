# This was created by Nihad
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def Conversion(request):
    text=request.GET.get('textfield','default')
    Check = request.GET.get('Doit','Off')
    print(Check)
    analyzed=''
    if Check=='on':
        for char in text:
            if 'a'<=char<='z':
                analyzed = analyzed + chr(ord(char)-97+65)
            else: analyzed = analyzed + char    
        dict={'purpose':'Without lowercase','analyzed':analyzed}
        return render(request,'result.html',dict)
    else :
        return HttpResponse('Please on the check button')
    