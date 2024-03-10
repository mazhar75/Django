# This was created by Nihad
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def Conversion(request):
    text = request.GET.get('textfield', 'default')
    check1 = request.GET.get('lower', 'off')
    check2 = request.GET.get('upper', 'off')
    check3 = request.GET.get('space', 'off')
    print(check1)

    # Dictionary to store conversion results
    results = {}

    if check1 == 'on':
        # Convert text to lowercase
        results['ToLow'] = text.lower()

    if check2 == 'on':
        # Convert text to uppercase
        results['ToHigh'] = text.upper()

    if check3 == 'on':
        # Remove extra spaces
        new_text = ''
        for index, char in enumerate(text):
            if char != ' ' or (index > 0 and text[index - 1] != ' '):
                new_text += char
        results['Space'] = new_text
    print(results)    

    return render(request, 'result.html', {'results': results})


    
            
            
                    
        
    