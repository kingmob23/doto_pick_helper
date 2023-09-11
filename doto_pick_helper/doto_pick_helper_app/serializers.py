from rest_framework import serializers

class Dota2DataSerializer(serializers.Serializer):
    hero_name = serializers.CharField()
    advantage_data = serializers.JSONField()
