from rest_framework import serializers
from .models import (
    Property,
    Feature,
    Amenity,
    PropertyAmenities,
    PropertyFeatures,
    PropertyLocation,
    PropertyMedia,
    Land,
    Building,
    Project,
    ProjectUnit,
    BookmarkedProperty
)
from apps.core.v1.models import PropertyType, PropertyUse
from apps.users.v1.models import User


# property location

class PropertyLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyLocation
        fields = "__all__"
        read_only_fields = ["property"]

# property media

class PropertyMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyMedia
        fields = "__all__"
        read_only_fields = ["property", "uploaded_at"]

# property land 

class LandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Land
        fields = "__all__"
        read_only_fields = ["property"]

# property Building

class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = "__all__"
        read_only_fields = ["property"]

# property project and project units

class ProjectUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectUnit
        fields = "__all__"
        read_only_fields = ["project"]


class ProjectSerializer(serializers.ModelSerializer):
    units = ProjectUnitSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = "__all__"



# property features and amenities 

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = "__all__"


class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = "__all__"

class PropertyFeatureSerializer(serializers.ModelSerializer):
    feature = FeatureSerializer(read_only=True)
    feature_id = serializers.PrimaryKeyRelatedField(
        queryset=Feature.objects.all(),
        source="feature",
        write_only=True
    )

    class Meta:
        model = PropertyFeatures
        fields = ["id", "feature", "feature_id"]


class PropertyAmenitySerializer(serializers.ModelSerializer):
    amenity = AmenitySerializer(read_only=True)
    amenity_id = serializers.PrimaryKeyRelatedField(
        queryset=Amenity.objects.all(),
        source="amenity",
        write_only=True
    )

    class Meta:
        model = PropertyAmenities
        fields = ["id", "amenity", "amenity_id"]


# property type and uses from the core app

class PropertyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyType
        fields = ["id", "name", "slug"]


class PropertyUseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyUse
        fields = ["id", "name", "slug"]


# property

# for searching
class PropertyListSerializer(serializers.ModelSerializer):
    property_type = PropertyTypeSerializer(read_only=True)
    property_use = PropertyUseSerializer(read_only=True)
    location = PropertyLocationSerializer(read_only=True)

    class Meta:
        model = Property
        fields = [
            "id",
            "title",
            "slug",
            "price",
            "negotiable",
            "property_status",
            "verified",
            "property_mode",
            "property_type",
            "property_use",
            "location",
        ]

class PropertyDetailSerializer(serializers.ModelSerializer):
    property_type = PropertyTypeSerializer(read_only=True)
    property_use = PropertyUseSerializer(read_only=True)
    location = PropertyLocationSerializer(read_only=True)
    media = PropertyMediaSerializer(many=True, read_only=True)
    features = PropertyFeatureSerializer(many=True, read_only=True)
    amenities = PropertyAmenitySerializer(many=True, read_only=True)
    land_details = LandSerializer(read_only=True)
    building_details = BuildingSerializer(read_only=True)
    projects = ProjectSerializer(many=True, read_only=True)

    listed_by = serializers.StringRelatedField()

    class Meta:
        model = Property
        fields = "__all__"

class PropertyCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = "__all__"
        read_only_fields = [
            "verified",
            "listed_date",
            "is_available",
            "listed_by",
        ]

# book mark

class BookmarkedPropertySerializer(serializers.ModelSerializer):
    property = PropertyListSerializer(read_only=True)

    class Meta:
        model = BookmarkedProperty
        fields = ["id", "property", "created_at"]


class BookmarkCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookmarkedProperty
        fields = ["property"]


