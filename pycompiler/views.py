import sys
from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request,'index.html')



def run(request):
    if request.method == 'POST':
        code_part = request.POST['codearea']
        input_part = request.POST['inputarea']
        y = input_part
        input_part = input_part.replace("\n"," ").split(" ")
        def input():
            a = input_part[0]
            del input_part[0]
            return a
        try:
            orig_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w')
            exec(code_part)
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = open('file.txt', 'r').read()
        except Exception as e:
            sys.stdout.close()
            sys.stdout=orig_stdout
            output = str(e)  
        return JsonResponse({"code": code_part, "input": y, "output": output})
