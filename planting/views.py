from django.http import HttpResponse
from django.shortcuts import render, redirect
from planting.models import *


def index(request):
    alex = User.objects.get(name = 'Alex')
    blake = User.objects.get(name = 'Blake')
    alex_yard = Yards.objects.filter(user_id = alex.id)
    blake_yard = Yards.objects.filter(user_id = blake.id)

    alex_plants = []
    #alex_plant_urls = []

    for y in alex_yard:
        alex_plants.append(Plant.objects.get(id = y.plant.id))

    #for x in alex_plants:
        #alex_plant_urls.append(x.imgURL)
        
    blake_plants = []
    #blake_plant_urls = []

    for y in blake_yard:
        blake_plants.append(Plant.objects.get(id = y.plant.id))

    #for x in blake_plants:
        #blake_plant_urls.append(x.imgURL)


    context = {
        'alexPlants': alex_plants,
        'blakePlants': blake_plants
        #'alexPlantUrls': alex_plant_urls,
        #'blakePlantUrls': blake_plant_urls
    }

    return render(request, 'planting/index.html', context)


def suggestions(request):
    #get list of all plantecosystem relationships that are deter or provide
    #for each of blake plants
        #get list of plantecosystemrelationships that are needs
            #for each n in list of blake-needs-plantecosystemrelationship
                #filter plantecosystems for provides of n platecosystemrelationships property
                    #add plant and relationship to context
        #get list of plantecosystemrelationships that are susceptible
            #for each n in list of blake-susceptible-plantecosystemrelationship
                #filter plantecosystems for deters of n platecosystemrelationships property
                    #add plant and relationship to context
                
    
    #Blake's <plant.name> <needs/is susceptible to> <shared property>. You can plant <suggestionplant.name> because it <provides/deters> <shared property> 
#     context = {
#         'relationship':
#             'blake_plant_name':  ,
#             'blake_plant_need': ,
#             'shared_plant_property': ,
#             'suggestion_plant_name':
#             'suggestion_plant_provides':
#     }
#    return render(request, 'planting/index.html', context)
    return render(request, 'planting/index.html')