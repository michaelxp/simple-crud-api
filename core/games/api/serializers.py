from rest_framework import serializers
from games import models


class GamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Games
        fields = '__all__'
