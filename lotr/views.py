from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponse
from .models import Character

def game(request):
    return HttpResponse("This is a main site of LOTR RPG Game!")

def detail(request, character_id):
    character = get_object_or_404(Character, pk=character_id)
    return render(request, 'lotr/detail.html', {'character': character})



