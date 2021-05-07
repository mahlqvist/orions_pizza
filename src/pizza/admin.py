from django.contrib import admin
from .models import PizzaType, Pizza, Size

admin.site.register(PizzaType)
admin.site.register(Pizza)
admin.site.register(Size)
