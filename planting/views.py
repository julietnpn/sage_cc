from django.http import HttpResponse
from django.shortcuts import render, redirect
from planting.models import *


def index(request):
    
    alex_plants = get_Alex_plants()
    blake_plants = get_Blake_plants()
    
    context = {
        'alexPlants': alex_plants,
        'blakePlants': blake_plants,
        'alexSuggestions': None,
    }
    return render(request, 'planting/index.html', context)


def suggestions(request):
    context = get_Alex_suggestions()
    return render(request, 'planting/index.html', context)


def get_Alex_suggestions():
    alex_plants = get_Blake_plants()
    blake_plants = get_Alex_plants()

    deterants = []
    providers = []
    needs = []

    
    #get list of all plantecosystem relationships that are deter and provide (value)
    # deter value in ERV is 1 and provides is 4, needs is 3, susceptible is 2

    all_plants = Plant.objects.all()

    for plant in all_plants:
        for d in PlantEcosystemRelationship.objects.filter( ecosystemRelationshipValue_id = 1):
            deterants.append(d)
        for p in PlantEcosystemRelationship.objects.filter( ecosystemRelationshipValue_id = 4):
            providers.append(p)

    blake_plant_needs = []
    blake_plant_susceptible = []

    for plant in blake_plants:
        for p in PlantEcosystemRelationship.objects.filter( plant = plant.id, ecosystemRelationshipValue_id = 3):
            blake_plant_needs.append(p)
        for s in PlantEcosystemRelationship.objects.filter( plant = plant.id, ecosystemRelationshipValue_id = 2):
            blake_plant_susceptible.append(s)

    alex_suggestions = []

    for need in blake_plant_needs:
        print ("need plant: " + need.plant.name)
        print ("property: " + need.ecosystemRelationshipProperty.attribute )
        print ("------------------------")
        for provide in providers:
            print ("provide plant: " + provide.plant.name)
            print ("property: " + provide.ecosystemRelationshipProperty.attribute )
            if need.ecosystemRelationshipProperty.attribute ==  provide.ecosystemRelationshipProperty.attribute:
                print("*************** MATCH #*******")
                alex_suggestions.append(provide.plant)


    for susceptible in blake_plant_susceptible:
        print ("susceptible plant: " + susceptible.plant.name)
        print ("property: " + susceptible.ecosystemRelationshipProperty.attribute )
        print ("------------------------")
        for deter in deterants:
            print ("deter plant: " + deter.plant.name)
            print ("property: " + deter.ecosystemRelationshipProperty.attribute )
            if susceptible.ecosystemRelationshipProperty.attribute ==  deter.ecosystemRelationshipProperty.attribute:
                print("*************** MATCH #*******")
                alex_suggestions.append(deter.plant)
                break

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
        'alexSuggestions': alex_suggestions,
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


def get_Alex_plants():
    alex = User.objects.get(name = 'Alex')
    alex_yard = Yards.objects.filter(user_id = alex.id)

    alex_plants = []

    for y in alex_yard:
        alex_plants.append(Plant.objects.get(id = y.plant.id))
    return alex_plants


def get_Blake_plants():
    blake = User.objects.get(name = 'Blake')

    blake_yard = Yards.objects.filter(user_id = blake.id)

    blake_plants = []
    
    for y in blake_yard:
        blake_plants.append(Plant.objects.get(id = y.plant.id))

    return blake_plants



