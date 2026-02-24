from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import PropertyType, PropertyUse, Channel, RelationshipStatus, Tag
from .serializers import (
    PropertyTypeSerializer,
    PropertyUseSerializer,
    ChannelSerializer,
    RelationshipStatusSerializer,
    TagSerializer
)


# PropertyType Views
class PropertyTypeListView(ListAPIView):
    queryset = PropertyType.objects.all()
    serializer_class = PropertyTypeSerializer
    permission_classes = [AllowAny]


class PropertyTypeCreateView(CreateAPIView):
    serializer_class = PropertyTypeSerializer
    permission_classes = [IsAuthenticated]


class PropertyTypeDetailView(RetrieveAPIView):
    queryset = PropertyType.objects.all()
    serializer_class = PropertyTypeSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "property_type_id"


class PropertyTypeUpdateView(UpdateAPIView):
    queryset = PropertyType.objects.all()
    serializer_class = PropertyTypeSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "property_type_id"


# PropertyUse Views
class PropertyUseListView(ListAPIView):
    queryset = PropertyUse.objects.all()
    serializer_class = PropertyUseSerializer
    permission_classes = [AllowAny]


class PropertyUseCreateView(CreateAPIView):
    serializer_class = PropertyUseSerializer
    permission_classes = [IsAuthenticated]


class PropertyUseDetailView(RetrieveAPIView):
    queryset = PropertyUse.objects.all()
    serializer_class = PropertyUseSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "property_use_id"


class PropertyUseUpdateView(UpdateAPIView):
    queryset = PropertyUse.objects.all()
    serializer_class = PropertyUseSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "property_use_id"


# Channel Views
class ChannelListView(ListAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
    permission_classes = [IsAuthenticated]


class ChannelCreateView(CreateAPIView):
    serializer_class = ChannelSerializer
    permission_classes = [IsAuthenticated]


class ChannelDetailView(RetrieveAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "channel_id"


class ChannelUpdateView(UpdateAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "channel_id"


# RelationshipStatus Views
class RelationshipStatusListView(ListAPIView):
    queryset = RelationshipStatus.objects.all()
    serializer_class = RelationshipStatusSerializer
    permission_classes = [IsAuthenticated]


class RelationshipStatusCreateView(CreateAPIView):
    serializer_class = RelationshipStatusSerializer
    permission_classes = [IsAuthenticated]


class RelationshipStatusDetailView(RetrieveAPIView):
    queryset = RelationshipStatus.objects.all()
    serializer_class = RelationshipStatusSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "relationship_status_id"


class RelationshipStatusUpdateView(UpdateAPIView):
    queryset = RelationshipStatus.objects.all()
    serializer_class = RelationshipStatusSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "relationship_status_id"


# Tag Views
class TagListView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]


class TagCreateView(CreateAPIView):
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]


class TagDetailView(RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "tag_id"


class TagUpdateView(UpdateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "tag_id"
