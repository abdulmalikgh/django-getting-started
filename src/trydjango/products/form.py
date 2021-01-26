from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = {
            'title',
            'description',
            'price'
        }

class RawProductForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea(attrs={"placeholder":'Enter your description'}))
    price = forms.DecimalField()
    summary = forms.CharField(widget=forms.Textarea(attrs={"placeholder":'Enter your summary'}))