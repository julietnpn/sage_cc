from django.http import HttpResponse


def index(request):
    alex = Users.objects.get(name = 'Alex')
    blake = Users.objects.get(name = 'Blake')
    alex_yard = Yards.objects.get(user_id = alex.id)
    blake_yard = Yards.objects.get(user_id = blake.id)
    #return HttpResponse("Hello, world. You're at the planting index.")
