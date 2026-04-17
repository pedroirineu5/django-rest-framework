from django.db.models import Avg
from rest_framework import serializers

from games.models import Games


class GamesSerializers(serializers.ModelSerializer):


    # Serlializer method field, isso é um campo que reconhece que ele vai ter uma função dentro da classe para calcula-lo
    # apenas sendo usado como um campo de GET, ou seja, leitura.
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Games
        fields = "__all__"

    def get_rate(self, obj):
        reviews = obj.reviews.aggregate(Avg('grade'))['grade__avg']
        
        if reviews:
            return round(reviews, 1)

        return None

    
    def validate_release_date(self, value):
        if value.year < 1962:
            raise serializers.ValidationError('A data de lançamento não pode ser menor que 1962')
        return value