from django.shortcuts import render

coins = [
        {'img': "../static/images/sample/sample-coin1.jpeg", 'denomination': "Half Peso", 'year': "1960", 'country': "Dominican Republic", 'for_sale': True, 'comment': "Mint condition"},
        {'img': "../static/images/sample/sample-coin2.jpeg", 'denomination': "Half Peso Silver", 'year': "1951", 'country': "Dominican Republic", 'for_sale': False, 'comment': "Mint condition"},
        {'img': "../static/images/sample/sample-coin3.jpeg", 'denomination': "25 Cents", 'year': "1963", 'country': "Dominican Republic", 'for_sale': False, 'comment': "Mint condition"}
]

def home(request):
    return render(request, 'extends/home.html', {
        'title': "Home",
        'coins': coins
    })

def about(request):
    return render(request, 'extends/about.html', {
        'title': "About"
    })
