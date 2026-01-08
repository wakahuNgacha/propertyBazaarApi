from rest_framework import serializers
from .models import *

class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = "__all__"

class CampaignCreateSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    updated_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Campaign
        exclude = ["created_at", "updated_at"]

class CampaignPerformanceMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignPerformanceMetric
        fields = "__all__"

class CampaignDocumentSerializer(serializers.ModelSerializer):
    uploaded_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = CampaignDocument
        fields = "__all__"

class CampaignChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignChannel
        fields = "__all__"

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = "__all__"

class ContentCreateSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    updated_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Content
        exclude = ["created_at", "updated_at"]

class BlogPostContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPostContent
        fields = "__all__"

class VideoContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoContent
        fields = "__all__"

class MediaAssetSerializer(serializers.ModelSerializer):
    uploaded_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = MediaAsset
        fields = "__all__"

class ContentTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentTag
        fields = "__all__"

class SocialChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialChannel
        fields = "__all__"

class SocialPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialPost
        fields = "__all__"

class SocialPostLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialPostLog
        fields = "__all__"

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = "__all__"

class SubscriberPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriberPreference
        fields = "__all__"

class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = "__all__"

class NewsletterCreateSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    updated_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Newsletter
        exclude = ["created_at", "updated_at"]

class NewsletterLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterLog
        fields = "__all__"

class EngagementEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngagementEvent
        fields = "__all__"

class EngagementEventCreateSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    updated_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = EngagementEvent
        exclude = ["created_at", "updated_at"]

class EngagementAttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngagementAttendee
        fields = "__all__"

class EngagementFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngagementFeedback
        fields = "__all__"

class ContentPerformanceSnapshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentPerformanceSnapshot
        fields = "__all__"

class CampaignContentPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignContentPerformance
        fields = "__all__"
