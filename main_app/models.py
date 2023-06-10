from django.db import models

class Coin(models.Model):
    img = models.TextField(max_length=300, default='../static/images/default-coin-img.gif')
    denomination = models.CharField(max_length=35)
    country = models.CharField(max_length=35)
    circulated = models.BooleanField()
    year = models.IntegerField()
    for_sale = models.BooleanField()
    condition = models.CharField(max_length=35)
    alloy = models.CharField(max_length=15, default='Unknown')
    details = models.TextField(max_length=500)

    def __str__(self):
        return self.country
