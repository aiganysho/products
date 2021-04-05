from django import forms

from webapp.models import Product, ProductInBasket, Order

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'category', 'description', 'remainder', 'price')


class ProductDeleteForm(forms.Form):
    name = forms.TimeField(required=True, label='Enter of the name, to delete! ')


class SearchForm(forms.Form):
    search_value = forms.CharField(max_length=100, required=False, label='Найти')


class ProductBasketForm(forms.ModelForm):
    class Meta:
        model = ProductInBasket
        fields = ('quantity',)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ( 'name_user', 'telephone', 'adress')


