from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Coin, Certification
from .forms import BiddingForm, CertificationForm

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
    id_list = coin.certifications.all().values_list('id')[:]
    certifications = []
    for id in id_list:
        certifications.append(Certification.objects.get(id=id[0]))
    bidding_form = BiddingForm()
    certification_form = CertificationForm()
    return render(request, 'extends/details.html', {
        'title': 'Details',
        'coin': coin,
        'certifications': certifications,
        'bidding_form': bidding_form,
        'certification_form': certification_form   
    })

def certifications(request):
    certifications = Certification.objects.all()
    return render(request, 'extends/certifications.html', {
        'title': "Certifications",
        'certifications': certifications
    })

def certification_detail(request, certification_id):
    certification = Certification.objects.get(id=certification_id), 
    return render(request, 'extends/certification.html', {
        'title': 'Certification',
        'certification': certification
    })

def add_certification(request, coin_id):
    form = CertificationForm(request.POST)
    if form.is_valid():
        new_certification = form.save(commit=False)
        new_certification.coin_id = coin_id
        new_certification.save()
        return redirect('detail', coin_id=coin_id)

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

class CertificationCreate(CreateView):
    model = Certification
    fields = '__all__'
    success_url = '/certifications'

class CertificationUpdate(UpdateView):
    model = Certification
    fields = '__all__'

class CertificationDelete(DeleteView):
    model = Certification
    success_url = '/certifications'