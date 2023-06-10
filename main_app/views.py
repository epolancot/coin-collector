from django.shortcuts import render
from .models import Coin

def coins_index(request):
    coins = Coin.objects.all()
    return render(request, 'extends/home.html', {
        'title': "Home",
        'coins': coins
    })

def coin_detail(request, coin_id):
    coin = Coin.objects.get(id=coin_id) 
    return render(request, 'extends/details.html', {
        'title': 'Details',
        'coin': coin
    })

def about(request):
    return render(request, 'extends/about.html', {
        'title': "About"
    })
