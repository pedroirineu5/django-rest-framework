from rest_framework import serializers

from games.models import Games


class GamesSerializers(serializers.DjangoModelField):
    model = Games
    fields = '__all__'