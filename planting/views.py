from django.http import HttpResponse
from django.shortcuts import render, redirect
from planting.models import *


def index(request):
    context = get_Alex_suggestions()
    return render(request, 'planting/index.html', context)


def suggestions(request):
    context = get_Alex_suggestions()
    return render(request, 'planting/index.html', context)


def get_Alex_suggestions():
    alex_plants = get_Alex_plants()
    blake_plants = get_Blake_plants()

    deterants = []
    providers = []
    needs = []

    

    
    #get list of all plantecosystem relationships that are deter and provide (value)
    # deter value in ERV is 1 and provides is 4, needs is 3, susceptible is 2

    all_plants = Plant.objects.all()

    for plant in all_plants:
        deterants.append(PlantEcosystemRelationship.objects.filter( ecosystemRelationshipValue_id = 1))
        providers.append(PlantEcosystemRelationship.objects.filter( ecosystemRelationshipValue_id = 4))


    blake_plant_needs = []
    blake_plant_susceptible = []

    for plant in blake_plants:
        blake_plant_needs.append(PlantEcosystemRelationship.objects.filter( ecosystemRelationshipValue_id = 3))
        blake_plant_susceptible.append(PlantEcosystemRelationship.objects.filter( ecosystemRelationshipValue_id = 2))


    alex_suggestions = []

    for plant in blake_plant_needs:
        for p in providers:
            if plant.ecosystemRelationshipProperty_id == p.ecosystemRelationshipProperty_id:
                alex_suggestions.append(plant)

    for plant in blake_plant_susceptible:
        for d in deterants:
            if plant.ecosystemRelationshipProperty_id == p.ecosystemRelationshipProperty_id:
                alex_suggestions.append(plant)



        

        

    #for each of blake plants
        #get list of plantecosystemrelationships that are needs
            #for each n in list of blake-needs-plantecosystemrelationship
                #filter plantecosystems for provides of n platecosystemrelationships property
                    #add plant and relationship to context
        #get list of plantecosystemrelationships that are susceptible
            #for each n in list of blake-susceptible-plantecosystemrelationship
                #filter plantecosystems for deters of n platecosystemrelationships property
                    #add plant and relationship to context
                


        context = {
        'alexPlants': alex_plants,
        'blakePlants': blake_plants,
        'alex_suggestions': alex_suggestions
        #'alexPlantUrls': alex_plant_urls,
        #'blakePlantUrls': blake_plant_urls
    }
    #Blake's <plant.name> <needs/is susceptible to> <shared property>. You can plant <suggestionplant.name> because it <provides/deters> <shared property> 
#     context = {
#         'relationship':
#             'blake_plant_name':  ,
#             'blake_plant_need': ,
#             'shared_plant_property': ,
#             'suggestion_plant_name':
#             'suggestion_plant_provides':
#     }

    return context
    #return render(request, 'planting/index.html')


def get_Alex_plants():
    alex = User.objects.get(name = 'Alex')
    alex_yard = Yards.objects.filter(user_id = alex.id)

    alex_plants = []
    #alex_plant_urls = []

    for y in alex_yard:
        alex_plants.append(Plant.objects.get(id = y.plant.id))

    #for x in alex_plants:
        #alex_plant_urls.append(x.imgURL)
        
    #blake_plant_urls = []

    

    #for x in blake_plants:
        #blake_plant_urls.append(x.imgURL)


def get_Blake_plants():
    blake = User.objects.get(name = 'Blake')

    blake_yard = Yards.objects.filter(user_id = blake.id)

    blake_plants = []
    
    for y in blake_yard:
        blake_plants.append(Plant.objects.get(id = y.plant.id))

    return blake_plants



