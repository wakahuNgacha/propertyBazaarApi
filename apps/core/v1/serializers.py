from rest_framework import serializers
from .models import PropertyType, PropertyUse, Channel, RelationshipStatus, Tag


class PropertyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyType
        fields = ["id", "name", "description"]


class PropertyUseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyUse
        fields = ["id", "name", "description"]


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ["id", "name", "description"]


class RelationshipStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelationshipStatus
        fields = ["id", "name", "description"]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name", "description"]
