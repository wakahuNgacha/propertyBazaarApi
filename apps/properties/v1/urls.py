from django.urls import path
from .views import *


urlpatterns = [
    path("properties/", PropertyListView.as_view()),
    path("properties/create/", PropertyCreateView.as_view()),
    path("properties/<slug:slug>/", PropertyDetailView.as_view()),
    path("properties/<slug:slug>/update/", PropertyUpdateView.as_view()),

    path("properties/<int:property_id>/location/", PropertyLocationCreateUpdateView.as_view()),
    path("properties/<int:property_id>/media/", PropertyMediaCreateView.as_view()),
    path("properties/<int:property_id>/land/", LandCreateUpdateView.as_view()),
    path("properties/<int:property_id>/building/", BuildingCreateUpdateView.as_view()),

    path("properties/<int:property_id>/projects/", ProjectCreateView.as_view()),
    path("projects/<int:project_id>/units/", ProjectUnitCreateView.as_view()),

    path("features/", FeatureListView.as_view()),
    path("features/create/", FeatureCreateView.as_view()),
    
    path("amenities/", AmenityListView.as_view()),
    path("amenities/create/", AmenityCreateView.as_view()),

    path("properties/<int:property_id>/features/add/", PropertyFeatureCreateView.as_view()),
    path("properties/<int:property_id>/amenities/add/", PropertyAmenityCreateView.as_view()),

    path("bookmarks/", UserBookmarksView.as_view()),
    path("bookmarks/add/", BookmarkCreateView.as_view()),
]
