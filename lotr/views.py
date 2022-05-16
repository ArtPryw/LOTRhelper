from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import Http404
from django.http import HttpResponse
from .models import Character

def game(request):
    return render(request, 'lotr/game.html')

def detail(request, character_id):
    character = get_object_or_404(Character, pk=character_id)
    return render(request, 'lotr/detail.html', {'character': character})

def heroes(request):
    heroes_list = Character.objects.all()
    template = loader.get_template('lotr/heroes.html')
    context = {
        'heroes_list': heroes_list,
    }
    return HttpResponse(template.render(context, request))



