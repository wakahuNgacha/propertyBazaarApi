from django.urls import path
from .views import (
    PropertyTypeListView,
    PropertyTypeCreateView,
    PropertyTypeDetailView,
    PropertyTypeUpdateView,
    PropertyUseListView,
    PropertyUseCreateView,
    PropertyUseDetailView,
    PropertyUseUpdateView,
    ChannelListView,
    ChannelCreateView,
    ChannelDetailView,
    ChannelUpdateView,
    RelationshipStatusListView,
    RelationshipStatusCreateView,
    RelationshipStatusDetailView,
    RelationshipStatusUpdateView,
    TagListView,
    TagCreateView,
    TagDetailView,
    TagUpdateView,
)

urlpatterns = [
    # PropertyType URLs
    path("property-types/", PropertyTypeListView.as_view()),
    path("property-types/create/", PropertyTypeCreateView.as_view()),
    path("property-types/<int:property_type_id>/", PropertyTypeDetailView.as_view()),
    path("property-types/<int:property_type_id>/update/", PropertyTypeUpdateView.as_view()),
    
    # PropertyUse URLs
    path("property-uses/", PropertyUseListView.as_view()),
    path("property-uses/create/", PropertyUseCreateView.as_view()),
    path("property-uses/<int:property_use_id>/", PropertyUseDetailView.as_view()),
    path("property-uses/<int:property_use_id>/update/", PropertyUseUpdateView.as_view()),
    
    # Channel URLs
    path("channels/", ChannelListView.as_view()),
    path("channels/create/", ChannelCreateView.as_view()),
    path("channels/<int:channel_id>/", ChannelDetailView.as_view()),
    path("channels/<int:channel_id>/update/", ChannelUpdateView.as_view()),
    
    # RelationshipStatus URLs
    path("relationship-statuses/", RelationshipStatusListView.as_view()),
    path("relationship-statuses/create/", RelationshipStatusCreateView.as_view()),
    path("relationship-statuses/<int:relationship_status_id>/", RelationshipStatusDetailView.as_view()),
    path("relationship-statuses/<int:relationship_status_id>/update/", RelationshipStatusUpdateView.as_view()),
    
    # Tag URLs
    path("tags/", TagListView.as_view()),
    path("tags/create/", TagCreateView.as_view()),
    path("tags/<int:tag_id>/", TagDetailView.as_view()),
    path("tags/<int:tag_id>/update/", TagUpdateView.as_view()),
]
