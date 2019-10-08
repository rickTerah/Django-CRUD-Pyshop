from django import forms
from .models import Product

# Create your forms here.
class ProductForm(forms.ModelForm):
    title = forms.CharField()
    price = forms.FloatField()
    stock = forms.IntegerField()

    class Meta:
        model = Product
        fields = [
            'title',
            'price',
            'stock'
        ]
