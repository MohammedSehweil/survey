from django.contrib import admin
from .models import Person
from .models import Products
from .models import Supermarket
# Register your models here.

admin.site.register(Person)
admin.site.register(Products)
admin.site.register(Supermarket)
