from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('pizzas', views.api_get_pizzas)
]
