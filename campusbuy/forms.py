from django import forms
from .models import Advert

class PostAdForm(forms.ModelForm):

    class Meta:
        model = Advert
        fields = ['category', 'Seller_Name', 'Item', 'image', 'Description', 'Asking_Price', 'Phone_Number', 'Location']
        widgets = {
            'Phone_Number': forms.TextInput(attrs={'placeholder': '+2347012345678'}),
        }