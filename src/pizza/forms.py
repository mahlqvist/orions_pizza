from django import forms
from .models import Pizza, PizzaType, Size

# Using Forms
# class PizzaForm(forms.Form):
#   SIZE_CHOICES = [('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')]
#   PIZZA_CHOICES= [('Margherita', 'Margherita'), ('Hawaii', 'Hawaii'), ('Pepperoni', 'Pepperoni'), ('BBQ Chicken', 'BBQ Chicken')]
#   pizza = forms.ChoiceField(label="", choices=PIZZA_CHOICES, initial=None, required=True)
#   size = forms.ChoiceField(label="", choices=SIZE_CHOICES)
#   extra = forms.CharField(label="Extra topping:", max_length=10, required=False)

# Using Model forms
class PizzaForm(forms.ModelForm):
  name = forms.ModelChoiceField(queryset=PizzaType.objects, empty_label="Choose pizza", label='', widget=forms.Select(attrs={'class': 'form-control', 'required': 'required'}))
  size = forms.ModelChoiceField(queryset=Size.objects, empty_label="Choose size", label='', widget=forms.Select(attrs={'class': 'form-control', 'required': 'required'}))
  class Meta:
    model = Pizza
    fields = ['name', 'size', 'extra']
    labels = {
      'extra': 'Extra Topping'
    }

class MultiplePizzaForm(forms.Form):
  amount = forms.IntegerField(min_value=2, max_value=4)
