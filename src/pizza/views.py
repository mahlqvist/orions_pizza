from django.shortcuts import render
from .forms import PizzaForm, MultiplePizzaForm
from .models import Pizza
from django.forms import formset_factory


def home(request):
  return render(request, 'home.html')


def order(request):
  multiple_form = MultiplePizzaForm()
  if request.method == 'POST':
    filled_form = PizzaForm(request.POST)
    if filled_form.is_valid():
      created_pizza = filled_form.save()
      created_pizza_key = created_pizza.id
      name = filled_form.cleaned_data["name"]
      size = filled_form.cleaned_data["size"]
      extra = filled_form.cleaned_data["extra"]
      msg = f"Your {size} {name} with extra {extra} is on its way!"
      if not extra:
        msg = f"Your {size} {name} is on its way!"
      note = f"Thank you for ordering! {msg}"
      filled_form = PizzaForm()
    else:
      created_pizza_key = None
      note = "Something went wrong, please try again." 
    return render(request, 'order.html', {
        'created_pizza_key': created_pizza_key,
        'pizzaform': filled_form,
        'note': note,
        'multiple_form': multiple_form
      })
  form = PizzaForm()
  return render(request, 'order.html', {
    'pizzaform': form,
    'multiple_form': multiple_form
  })

def pizzas(request):
  amount = 2
  filled_multiple_form = MultiplePizzaForm(request.GET)
  if filled_multiple_form.is_valid():
    amount = filled_multiple_form.cleaned_data["amount"]
  PizzaFormSet = formset_factory(PizzaForm, extra=amount)
  formset = PizzaFormSet()
  note = ''
  if request.method == 'POST':
    filled_formset = PizzaFormSet(request.POST)
    if filled_formset.is_valid():
      for form in filled_formset:
        print(form.cleaned_data["name"])
      note = "Pizzas have been ordered"
    else:
      note= "Something went wrong"
    return render(request, 'pizzas.html', {
      'note': note,
      'formset': formset
    })
  else:
    return render(request, 'pizzas.html', {
      'formset': formset
    })

def edit_order(request, pizza_id):
  pizza = Pizza.objects.get(id=pizza_id)
  form = PizzaForm(instance=pizza)
  note = ''
  if request.method == 'POST':
    filled_form = PizzaForm(request.POST, instance=pizza)
    if filled_form.is_valid():
      filled_form.save()
      note = "The order has been updated"
      form = filled_form
    else:
      note = "The order was not changed"
  return render(request, 'edit_order.html', {
    'note': note,
    'pizzaform': form,
    'pizza': pizza
  })