from webbrowser import register

from django.contrib import admin
from django.contrib.auth.models import Permission

from GameLibrary.models import Game, Game_type, Image

# Register your models here.
admin.site.register(Game)
admin.site.register(Image)
admin.site.register(Game_type)

admin.site.register(Permission)