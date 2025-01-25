from django.contrib import admin
from .models import Pizza, Pasta

class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name', 'ingredients', 'price', 'vegan')
    search_fields = ('name', 'ingredients')

class PastaAdmin(admin.ModelAdmin):
    list_display = ('name', 'ingredients', 'price')
    search_fields = ('name', 'ingredients')

# Register your models here.
admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Pasta, PastaAdmin)
