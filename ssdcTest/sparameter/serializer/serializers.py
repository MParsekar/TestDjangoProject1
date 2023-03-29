from ..dto import models
from rest_framework import serializers
from rest_framework.fields import IntegerField


class SprameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sprameterdata
        fields = '__all__'
