from .models import Auction
from django import forms

# fornisce form per pubblicazione di post a disposizione dell'utente


class auctionForm(forms.ModelForm):

    class Meta:
        model = Auction
        fields = ('title', 'text', 'startPrice', 'image')


class bidForm(forms.ModelForm):

    class Meta:
        model = Auction
        fields = ('endPrice',)


class detailForm(forms.ModelForm):

    class Meta:
        model = Auction
        fields = ("id",)
