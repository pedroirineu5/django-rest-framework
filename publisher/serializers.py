from rest_framework import serializers

from publisher.models import Publisher


class PublisherSerializers(serializers.ModelSerializer):
    model = Publisher
    fields = '__all__'