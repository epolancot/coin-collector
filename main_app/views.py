from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Coin
from .forms import BiddingForm

def index(request):
    coins = Coin.objects.all()
    return render(request, 'extends/home.html', {
        'title': "Home",
        'coins': coins
    })

def home(request):
    coins = Coin.objects.all()
    return render(request, 'extends/home.html', {
        'title': "Home",
        'coins': coins
    })

def coin_detail(request, coin_id):
    coin = Coin.objects.get(id=coin_id) 
    bidding_form = BiddingForm()
    return render(request, 'extends/details.html', {
        'title': 'Details',
        'coin': coin,
        'bidding_form': bidding_form
        
    })

def add_bid(request, coin_id):
 # create a ModelForm instance using the data in request.POST
  form = BiddingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_bidding = form.save(commit=False)
    new_bidding.coin_id = coin_id
    new_bidding.save()
    return redirect('detail', coin_id=coin_id)

def about(request):
    return render(request, 'extends/about.html', {
        'title': "About"
    })


class CoinCreate(CreateView):
    model = Coin
    fields = '__all__'

class CoinUpdate(UpdateView):
    model = Coin
    fields = '__all__'

class CoinDelete(DeleteView):
    model = Coin
    success_url = '/coins'