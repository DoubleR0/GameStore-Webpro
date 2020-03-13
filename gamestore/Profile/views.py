import random
from builtins import object

from django.contrib.auth import logout
from django.shortcuts import redirect, render

from GameLibrary.models import Game, Image, User_games


# Create your views here.
def myGame(request):
    user = request.user
    usergame = User_games.objects.filter(user_id_id=user.id)
    image = Image.objects.all()
    print(usergame)
    game = Game.objects.all()
    
    return render(request, template_name='Profile/MyGame.html', context={
        "usergame":usergame,
        "game":game,
        "image":image,
    })

def payment(request, id):
    return render(request, template_name='Profile/payment.html', context={
        "id":id
    })

def buy(request, id):
    user = request.user
    if request.method=="POST":
        game = User_games(
            serial='%32x' % random.getrandbits(16*8),
            user_id_id=user.id,
            game_id_id=id
        )
        game.save()
    return redirect("index")


def logouted(request):
    logout(request)
    return redirect("index")
