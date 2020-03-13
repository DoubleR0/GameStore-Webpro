from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Game_type(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=50)

    def __str__(self):
        return self.type_name

class Game(models.Model):
    game_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    game_type_id = models.ForeignKey(Game_type, on_delete=models.CASCADE)
    developer = models.CharField(max_length=50)
    rating = models.CharField(max_length=50)
    release_date = models.DateField(auto_now=False, auto_now_add=False)
    price = models.FloatField()

    def __str__(self):
        return self.name

class User_games(models.Model):
    user_game_id =  models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    game_id = models.ForeignKey(Game,on_delete=models.CASCADE)
    purchased_date = models.DateTimeField(auto_now_add=True)
    serial = models.CharField(max_length=50)

    def __str__(self):
        return self.serial
    

class Image(models.Model):
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    image_url = models.ImageField(upload_to="ImageGame", height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return "%s" % self.game_id.name

    