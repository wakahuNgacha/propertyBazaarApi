from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Property, Feature, Amenity, PropertyFeatures, PropertyAmenities
from .serializers import *

# Create your views here.

class PropertyListView(ListAPIView):
    queryset = (
        Property.objects
        .filter(property_status="available", is_available=True)
        .select_related("property_type", "property_use")
        .prefetch_related("location", "media")
    )
    serializer_class = PropertyListSerializer

class PropertyDetailView(RetrieveAPIView):
    queryset = (
        Property.objects
        .select_related("property_type", "property_use", "location", "listed_by")
        .prefetch_related(
            "media",
            "features__feature",
            "amenities__amenity",
            "projects__units"
        )
    )
    serializer_class = PropertyDetailSerializer
    lookup_field = "slug"

class PropertyCreateView(CreateAPIView):
    serializer_class = PropertyCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(listed_by=self.request.user)

class PropertyUpdateView(UpdateAPIView):
    serializer_class = PropertyCreateUpdateSerializer
    permission_classes = [IsAuthenticated]
    queryset = Property.objects.all()
    lookup_field = "slug"

class PropertyLocationCreateUpdateView(CreateAPIView, UpdateAPIView):
    serializer_class = PropertyLocationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(property_id=self.kwargs["property_id"])

class PropertyMediaCreateView(CreateAPIView):
    serializer_class = PropertyMediaSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(property_id=self.kwargs["property_id"])

class PropertyMediaCreateView(CreateAPIView):
    serializer_class = PropertyMediaSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(property_id=self.kwargs["property_id"])

class LandCreateUpdateView(CreateAPIView, UpdateAPIView):
    serializer_class = LandSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(property_id=self.kwargs["property_id"])

class BuildingCreateUpdateView(CreateAPIView, UpdateAPIView):
    serializer_class = BuildingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(property_id=self.kwargs["property_id"])

class ProjectCreateView(CreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(property_id=self.kwargs["property_id"])

class ProjectUnitCreateView(CreateAPIView):
    serializer_class = ProjectUnitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(project_id=self.kwargs["project_id"])

class FeatureListView(ListAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    permission_classes = [IsAuthenticated]


class FeatureCreateView(CreateAPIView):
    serializer_class = FeatureSerializer
    permission_classes = [IsAuthenticated]


class AmenityListView(ListAPIView):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer
    permission_classes = [IsAuthenticated]


class AmenityCreateView(CreateAPIView):
    serializer_class = AmenitySerializer
    permission_classes = [IsAuthenticated]


class PropertyFeatureCreateView(CreateAPIView):
    serializer_class = PropertyFeatureSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(property_id=self.kwargs["property_id"])


class PropertyAmenityCreateView(CreateAPIView):
    serializer_class = PropertyAmenitySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(property_id=self.kwargs["property_id"])

class BookmarkCreateView(CreateAPIView):
    serializer_class = BookmarkCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserBookmarksView(ListAPIView):
    serializer_class = BookmarkedPropertySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return BookmarkedProperty.objects.filter(user=self.request.user)

