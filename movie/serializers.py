from rest_framework import serializers
from .models import Movie


class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'owner', 'name', 'description', 'created_at', 'updated_at')