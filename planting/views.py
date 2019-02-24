from django.http import HttpResponse
from django.shortcuts import render, redirect
from planting.models import *


def index(request):
    alex = User.objects.get(name = 'Alex')
    blake = User.objects.get(name = 'Blake')
    alex_yard = Yards.objects.filter(user_id = alex.id)
    blake_yard = Yards.objects.filter(user_id = blake.id)

    alex_plants = []
    alex_plant_urls = []

    for y in alex_yard:
        alex_plants.append(Plant.objects.get(id = y.plant.id))

    for x in alex_plants:
        alex_plant_urls.append(x.imgURL)
        
    blake_plants = []
    blake_plant_urls = []

    for y in blake_yard:
        blake_plants.append(Plant.objects.get(id = y.plant.id))

    for x in blake_plants:
        blake_plant_urls.append(x.imgURL)


    context = {
        'alexPlantUrls': alex_plant_urls,
        'blakePlantUrls': blake_plant_urls
    }

    return render(request, 'planting/index.html', context)

def suggestions(request):
    return HttpResponse("Hello, world. Here are suggestions.")