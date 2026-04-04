from rest_framework import serializers

from genres.models import Genre


#                                   v O model serialiser presta para n ter que ficar marcando todos o atributos do model, por exemplo.  
# Aquele Class lá em baixo. Você está basicamente escrevendo o seguinte:
# name = model.charfield(max_caracters=200)
# exemplo = models.intergerfiled()
class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        # aqui está apontando qual o model que ele vai trabalhar e tbm o model que será "copiado"
        model = Genre
        # aqui ele está copiando todos os campos do model para n fazer o trabalho de quenga lá em cima ^^
        fields = "__all__"

        