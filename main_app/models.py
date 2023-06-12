from django.db import models
from django.urls import reverse
from django.utils import timezone


COUNTRIES = (
    ('DOM', 'Dominican Republic'),
    ('USA', 'United States')
)

CONDITION = (
    ('M', 'Mint State'), 
    ('G', 'Good'), 
    ('F', 'Fair'), 
    ('P', 'Poor')
)

class Coin(models.Model):
    img = models.TextField(max_length=300, default='../static/images/default-coin-img.gif')
    denomination = models.CharField(max_length=35)
    country = models.CharField(
        max_length=3,
        choices=COUNTRIES,
        default=COUNTRIES[0][0])
    circulated = models.BooleanField()
    year = models.IntegerField()
    for_sale = models.BooleanField()
    condition = models.CharField(
        max_length=1,
        choices=CONDITION,
        default=CONDITION[0][0])
    alloy = models.CharField(max_length=15, default='Unknown')
    details = models.TextField(max_length=500)

    def __str__(self):
        return self.country
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'coin_id': self.id})
    
class Bid(models.Model):
    date = models.DateField(("Date"),
            default = timezone.now)
    amount = models.IntegerField()
    comment = models.TextField(max_length=500)
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)

    # def __str__(self):
    #     return f"${self.get_amount_display()} on {self.date}"
