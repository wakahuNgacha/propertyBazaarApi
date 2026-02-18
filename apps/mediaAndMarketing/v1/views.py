from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView
)
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import *
from .serializers import *


# Create your views here.
class CampaignListView(ListAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    permission_classes = [IsAuthenticated]

class CampaignCreateView(CreateAPIView):
    serializer_class = CampaignCreateSerializer
    permission_classes = [IsAuthenticated]

class CampaignDetailView(RetrieveAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    lookup_field = "id"
    permission_classes = [IsAuthenticated]

class CampaignUpdateView(UpdateAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignCreateSerializer
    lookup_field = "id"
    permission_classes = [IsAuthenticated]

class CampaignPerformanceMetricCreateView(CreateAPIView):
    serializer_class = CampaignPerformanceMetricSerializer
    permission_classes = [IsAuthenticated]

class CampaignDocumentCreateView(CreateAPIView):
    serializer_class = CampaignDocumentSerializer
    permission_classes = [IsAuthenticated]

class CampaignDocumentListView(ListAPIView):
    queryset = CampaignDocument.objects.all()
    serializer_class = CampaignDocumentSerializer
    permission_classes = [IsAuthenticated]

class CampaignChannelCreateView(CreateAPIView):
    serializer_class = CampaignChannelSerializer
    permission_classes = [IsAuthenticated]


class ContentListView(ListAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = [IsAuthenticated]

class ContentCreateView(CreateAPIView):
    serializer_class = ContentCreateSerializer
    permission_classes = [IsAuthenticated]

class ContentDetailView(RetrieveAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_field = "slug"
    permission_classes = [IsAuthenticated]

class ContentUpdateView(UpdateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentCreateSerializer
    lookup_field = "slug"
    permission_classes = [IsAuthenticated]

class BlogPostContentCreateView(CreateAPIView):
    serializer_class = BlogPostContentSerializer
    permission_classes = [IsAuthenticated]

class VideoContentCreateView(CreateAPIView):
    serializer_class = VideoContentSerializer
    permission_classes = [IsAuthenticated]

class VideoContentListView(ListAPIView):
    queryset = VideoContent.objects.all()
    serializer_class = VideoContentSerializer
    permission_classes = [IsAuthenticated]

class MediaAssetCreateView(CreateAPIView):
    serializer_class = MediaAssetSerializer
    permission_classes = [IsAuthenticated]

class MediaAssetListView(ListAPIView):
    queryset = MediaAsset.objects.all()
    serializer_class = MediaAssetSerializer
    permission_classes = [IsAuthenticated]

class ContentTagCreateView(CreateAPIView):
    serializer_class = ContentTagSerializer
    permission_classes = [IsAuthenticated]

class SocialChannelListView(ListAPIView):
    queryset = SocialChannel.objects.all()
    serializer_class = SocialChannelListSerializer
    permission_classes = [IsAuthenticated]

class SocialChannelCreateView(CreateAPIView):
    serializer_class = SocialChannelSerializer
    permission_classes = [IsAuthenticated]

class SocialPostCreateView(CreateAPIView):
    serializer_class = SocialPostSerializer
    permission_classes = [IsAuthenticated]

class SocialPostListView(ListAPIView):
    queryset = SocialPost.objects.all()
    serializer_class = SocialPostSerializer
    permission_classes = [IsAuthenticated]

class SocialPostLogCreateView(CreateAPIView):
    serializer_class = SocialPostLogSerializer
    permission_classes = [IsAuthenticated]

class SubscriberListView(ListAPIView):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer

class SubscriberCreateView(CreateAPIView):
    serializer_class = SubscriberSerializer

class SubscriberPreferenceCreateView(CreateAPIView):
    serializer_class = SubscriberPreferenceSerializer
    permission_classes = [IsAuthenticated]

class NewsletterListView(ListAPIView):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
    permission_classes = [IsAuthenticated]

class NewsletterCreateView(CreateAPIView):
    serializer_class = NewsletterCreateSerializer
    permission_classes = [IsAuthenticated]

class NewsletterLogCreateView(CreateAPIView):
    serializer_class = NewsletterLogSerializer
    permission_classes = [IsAuthenticated]

class EngagementEventListView(ListAPIView):
    queryset = EngagementEvent.objects.all()
    serializer_class = EngagementEventSerializer
    permission_classes = [IsAuthenticated]

class EngagementEventCreateView(CreateAPIView):
    serializer_class = EngagementEventCreateSerializer
    permission_classes = [IsAuthenticated]

class EngagementAttendeeCreateView(CreateAPIView):
    serializer_class = EngagementAttendeeSerializer
    permission_classes = [IsAuthenticated]

class EngagementFeedbackCreateView(CreateAPIView):
    serializer_class = EngagementFeedbackSerializer
    permission_classes = [IsAuthenticated]

class ContentPerformanceSnapshotCreateView(CreateAPIView):
    serializer_class = ContentPerformanceSnapshotSerializer
    permission_classes = [IsAuthenticated]

class CampaignContentPerformanceCreateView(CreateAPIView):
    serializer_class = CampaignContentPerformanceSerializer
    permission_classes = [IsAuthenticated]


