from django.db import models

from developers.models import Developers
from genres.models import Genre


class GamesModel(models.Model):

    # name_game = models.CharField(max_length=200)
    # genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='game_genre')
    # developer = models.ManyToManyField(Developers, on_delete=models.PROTECT, related_name='game_devs')
    # publisher = models.ForeignKey()
    # release_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name