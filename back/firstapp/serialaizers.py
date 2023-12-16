from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer, CharField
from firstapp.models import Games1

class Games1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Games1
        fields = ["id", "name", "production", "disrtibutor", "genre", "price", "publication_data"]