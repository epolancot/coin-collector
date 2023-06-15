from django.contrib import admin
from .models import Coin, Bid, Certification

admin.site.register(Coin)
admin.site.register(Bid)
admin.site.register(Certification)

