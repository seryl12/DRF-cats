from rest_framework import serializers


class CatSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=16)
    color = serializers.CharField(max_length=16)
    year_of_birth = serializers.IntegerField(min_value=1)
