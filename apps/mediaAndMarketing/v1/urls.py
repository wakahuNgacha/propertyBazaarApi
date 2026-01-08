from django.urls import path
from .views import *

urlpatterns = [
    # CAMPAIGNS
    path("campaigns/", CampaignListView.as_view()),
    path("campaigns/create/", CampaignCreateView.as_view()),
    path("campaigns/<int:id>/", CampaignDetailView.as_view()),
    path("campaigns/<int:id>/update/", CampaignUpdateView.as_view()),
    # Campaign channels, documents & metrics
    path("campaigns/metrics/create/", CampaignPerformanceMetricCreateView.as_view()),
    path("campaigns/documents/create/", CampaignDocumentCreateView.as_view()),
    path("campaigns/channels/create/", CampaignChannelCreateView.as_view()),

    # CONTENT
    path("content/", ContentListView.as_view()),
    path("content/create/", ContentCreateView.as_view()),
    path("content/<slug:slug>/", ContentDetailView.as_view()),
    path("content/<slug:slug>/update/", ContentUpdateView.as_view()),
    # Blog & Video content extensions
    path("content/blog/create/", BlogPostContentCreateView.as_view()),
    path("content/video/create/", VideoContentCreateView.as_view()),
    # Media & tags
    path("content/media/create/", MediaAssetCreateView.as_view()),
    path("content/tags/create/", ContentTagCreateView.as_view()),

    # SOCIAL MEDIA
    path("social/channels/", SocialChannelListView.as_view()),
    path("social/channels/create/", SocialChannelCreateView.as_view()),

    path("social/posts/create/", SocialPostCreateView.as_view()),
    path("social/posts/logs/create/", SocialPostLogCreateView.as_view()),

    # EMAIL MARKETING
    path("subscribers/", SubscriberListView.as_view()),
    path("subscribers/create/", SubscriberCreateView.as_view()),

    path("subscribers/preferences/create/", SubscriberPreferenceCreateView.as_view()),

    path("newsletters/", NewsletterListView.as_view()),
    path("newsletters/create/", NewsletterCreateView.as_view()),
    path("newsletters/logs/create/", NewsletterLogCreateView.as_view()),

    # ENGAGEMENT EVENTS
    path("engagement-events/", EngagementEventListView.as_view()),
    path("engagement-events/create/", EngagementEventCreateView.as_view()),

    path("engagement-events/attendees/create/", EngagementAttendeeCreateView.as_view()),
    path("engagement-events/feedback/create/", EngagementFeedbackCreateView.as_view()),

    # PERFORMANCE METRICS
    path("performance/content/create/", ContentPerformanceSnapshotCreateView.as_view()),
    path("performance/campaign/create/", CampaignContentPerformanceCreateView.as_view()),

]
