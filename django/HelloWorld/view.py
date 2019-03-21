from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    context = {}
    context['h1'] = 'hello world'
    # context['p'] = '这是一个段落'
    return render(request, 'hello.html',context)
    # return HttpResponse("Hello World !")
