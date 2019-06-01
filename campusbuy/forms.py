from django import forms
from .models import Advert


class PostAdForm(forms.ModelForm):

    class Meta:
        model = Advert
        fields = ['category', 'Seller_Name', 'image', 'Item', 'Description', 'Asking_Price', 'Phone_Number', 'Location']
