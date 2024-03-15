from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def interface(request):
    text = request.POST.get('textfield', 'You did not enter text')
    key = request.POST.get('key', '0')
    en = request.POST.get('en', 'de')
    print(key)
    print("Text:", text)
    print("Key:", key)
    print("Encryption:", en)
    k=10
    try:
        k=int(key)
        k=k%26
    except ValueError:
        return HttpResponse('Plaese Enter a valid key') 
    dict={}
    result='' 
    if en=='en':
        #l=len(text)
        for char in text:
            if 'a'<=char<='z':
                result = result + chr((ord(char)-97+k)%26+97)
            elif 'A'<=char<='Z':
                result = result + chr((ord(char)-65+k)%26+65)
            else :
                result = result + char
        dict['H']='Encrypted text'
        dict['res']=result           
                        
    else:
        for char in text:
            if 'a'<=char<='z':
                result = result + chr((ord(char)-97-k+26)%26+97)
            elif 'A'<=char<='Z':
                result = result + chr((ord(char)-65-k+26)%26+65)
            else :
                result = result + char  
        dict['H']='Decrypted text'
        dict['res']=result                 
    
    return render(request,'result.html',dict)
