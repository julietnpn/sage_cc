from django.http import HttpResponse


def index(request):
    alex = Users.objects.get(name = 'Alex')
    blake = Users.objects.get(name = 'Blake')
    alex_yard = Yards.objects.get(user_id = alex.id)
    blake_yard = Yards.objects.get(user_id = blake.id)
    #return HttpResponse("Hello, world. You're at the planting index.")

alex_plants = []
alex_plant_urls = []

for y in alex_yard:
    alex_plants.append(Plant.objects.get(id = alex_yard.plant))

for x in alex_plants:
    plant_urls.append(Plant.objects.get(imgURL))


context = {
    'alexPlantUrls': alex_plant_urls
}    

                    
#return HttpResponse("Hello, world. You're at the planting index.")