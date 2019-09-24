from django import forms
from .models import Advert


class PostAdForm(forms.ModelForm):

    class Meta:
        model = Advert
        fields = ['Seller_Name', 'category', 'Item', 'Asking_Price',
                  'Description', 'image',  'Phone_Number', 'Location']
