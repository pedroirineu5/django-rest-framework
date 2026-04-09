from django.db import models

from developers.models import Developers
from genres.models import Genre
from platforms.models import Platforms
from publisher.models import Publisher


class Games(models.Model):

    name_game = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
    developers = models.ManyToManyField(Developers)
    publisher = models.ForeignKey(Publisher,on_delete=models.PROTECT)
    platform = models.ManyToManyField(Platforms)
    release_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name_game