from django.shortcuts import render

def index(request):
    return render(request,'blog/hendi.html')

def hendi(request):
    ashraf='this is ashraf'
    return render(request,'blog/hendy.html',{'x':ashraf})
