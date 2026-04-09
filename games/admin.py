from django.contrib import admin
from games.models import Games

# Register your models here.

@admin.register(Games)
class GamesAdmin(admin.ModelAdmin):
    list_display = ('name_game','genre','publisher', 'release_date')

