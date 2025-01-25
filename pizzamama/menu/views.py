from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Pizza, Pasta

# Create your views here.
def index(request):
    # p = Pizza.objects.all()
    # pizzas = ", ".join([p.name + " : " + str(p.price) + "€" for p in p])
    # return HttpResponse(pizzas)
    return render(request, 'menu/index.html', {
        'pizzas': Pizza.objects.all().order_by('price'),
        'pastas': Pasta.objects.all().order_by('price')
    })

def api_get_pizzas(request):
    pizzas = Pizza.objects.all()
    json_pizzas = serializers.serialize('json', pizzas)
    return HttpResponse(json_pizzas)
