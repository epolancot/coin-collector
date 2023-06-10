from django.shortcuts import render

def home(request):
    return render(request, 'extends/home.html', {
        'title': "Home"
    })

def about(request):
    return render(request, 'extends/about.html', {
        'title': "About"
    })
