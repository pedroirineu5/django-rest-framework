from rest_framework import serializers

from platforms.models import Platforms


class PlatformSerializers(serializers.ModelSerializer):
    class Meta:
        model = Platforms
        fields = '__all__'