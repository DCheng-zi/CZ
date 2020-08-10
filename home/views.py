from django.shortcuts import render

def home(request):
    '''加载前端'''
    return render(request,'index.html')