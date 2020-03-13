from builtins import object
from multiprocessing.sharedctypes import Value
from optparse import Values
from os.path import exists
from django.db.models import Q
from django.shortcuts import render
from GameLibrary.models import Game, Game_type, Image, User_games


# Create your views here.
def index(request):
    listgame = []
    alltype = []
    # qerry
    # user = User.objects.filter(user_id=1)
    # save to database
    # user = User(username="ham", password="1234", first_name="ham", last_name="ham", email="ham@email.com")
    # user.save()
    game_type = Game_type.objects.all().values()
    game = Game.objects.all().values()
    image = Image.objects.all().values()
    user = request.user
    typer = "Normal"

    for i in game_type:
        if(Game.objects.filter(game_type_id = i["type_id"]).exists()):
            alltype.append(i)
            count = 0
            for j in game:
                if(j["game_type_id_id"] == i["type_id"] and count < 5):
                    count += 1
                    listgame.append(j)
    print(alltype)
    print(listgame)

    if request.method=="POST":
        text = request.POST.get("Search")
        if(text==''):
            game = Game.objects.all().values()
            image = Image.objects.all().values()
        else:
            game = Game.objects.filter(Q(name__contains=text)|Q(developer__contains=text))
            image = Image.objects.all().values()
        typer = "Search"


    return render(request, template_name='GameLibrary/homePage.html', context={
        "listgame": listgame,
        "image": image,
        "game_type": game_type,
        "alltype":alltype,
        "user":user,
        "type": typer
    })

def detail(request, id):
    user = request.user
    buyed = ""
    buy = User_games.objects.filter(user_id_id=user.id)
    game = Game.objects.get(pk=id)
    image = Image.objects.get(game_id=id)
    print(image)
    for i in buy:
        print(i.game_id_id)
        if(i.game_id_id == id):
            buyed = "mute"

    return render(request, template_name='GameLibrary/gameDetail.html', context={
        "game": game,
        "image": image,
        "user":user,
        "buyed":buyed
    })

def category(request):
    listgame = []
    list_check = []
    sli = 0
    alltype = []
    user = request.user
    game_type = Game_type.objects.all().values()
    game = Game.objects.all().values()
    image = Image.objects.all().values()

    if request.method=="POST":
        for i in game_type:
            gamet_id = str(i["type_id"])
            list_check.append(request.POST.get(str(i["type_id"])))
        for i in list_check:
            if(i != None):
                sli = list_check.index(i)
        check = list_check[sli:sli+1]
        print(check)
        for i in game:
            if(i["game_type_id_id"] == int(check[0])):
                listgame.append(i)
        print(listgame)
        for i in game_type:
            if(Game.objects.filter(game_type_id = i["type_id"]).exists()):
                alltype.append(i)

    return render(request, template_name='GameLibrary/category.html', context={
        "check":int(check[0]),
        "listgame": listgame,
        "image": image,
        "game_type": game_type,
        "alltype":alltype,
        "user":user
    })
