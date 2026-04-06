from rest_framework import serializers

from developers.models import Developers


class DevelopersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Developers
        fields = '__all__'