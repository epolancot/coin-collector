from django.shortcuts import render

def home(request):
    return render(request, 'extends/home.html')

def about(request):
    return render(request, 'extends/about.html')
