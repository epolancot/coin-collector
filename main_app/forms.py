from django.forms import ModelForm
from .models import Bid, Certification

class BiddingForm(ModelForm):
  class Meta:
    model = Bid
    fields = ['amount', 'comment']

class CertificationForm(ModelForm):
    class Meta:
      model = Certification
      fields = '__all__'