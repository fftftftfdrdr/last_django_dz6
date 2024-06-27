from django.shortcuts import render
from random import randint
from .models import RandomNumber

def random_number_view(request):
    number = randint(1, 100)
    RandomNumber.objects.create(number=number)
    return render(request, 'random_number.html', {'number': number})
   
