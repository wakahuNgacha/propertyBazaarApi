from django.db import models
from apps.users.v1.models import User
from apps.properties.v1.models import Property
from apps.core.v1.models import Channel, Tag, PropertyType

# Create your models here.
class Campaign(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('Planned', 'Planned'),  
        ('Active', 'Active'),
        ('Paused', 'Paused'),  
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]
    TYPE_CHOICES = [
        # promotional when it's linked to a property sale so the measure of success is tied to the sale
        ('promotional', 'Promotional'),
        # editorial when it's general content
        ('editorial', 'Editorial'),
    ]
    name = models.CharField(max_length=255)
    objective = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    start_date = models.DateField()
    end_date = models.DateField()
    type = models.CharField(max_length=100, choices=TYPE_CHOICES, default='editorial')
    property = models.ForeignKey(Property, on_delete=models.SET_NULL, null=True, blank=True, related_name='campaigns')
    budget_estimate = models.DecimalField(max_digits=10, decimal_places=2)
    budget_actual = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='campaigns_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='campaigns_updated')

    def __str__(self):
        return self.name

class CampaignPerformanceMetric(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='performance_metrics')
    metric_name = models.CharField(max_length=100)
    metric_value = models.DecimalField(max_digits=15, decimal_places=2)
    recorded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.metric_name} for {self.campaign.name} at {self.recorded_at}"

    
class CampaignDocument(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='documents')
    file = models.URLField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='campaign_documents_uploaded')

    def __str__(self):
        return f"Document for {self.campaign.name} uploaded at {self.uploaded_at}"
    
class CampaignChannel(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='channels')
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name='campaigns')
    allocated_budget = models.DecimalField(max_digits=10, decimal_places=2)
    actual_spend = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.channel.name} for {self.campaign.name}"
    

class Content(models.Model):
    CONTENT_TYPE_CHOICES = [
        ('blog_post', 'Blog Post'),
        ('social_media', 'Social Media'),
        ('video', 'Video'),
        ('infographic', 'Infographic'),
    ]
    content_type = models.CharField(max_length=50, choices=CONTENT_TYPE_CHOICES)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='contents')
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    summary = models.TextField()
    status = models.CharField(max_length=20, choices=Campaign.STATUS_CHOICES, default='draft')
    featured = models.BooleanField(default=False)
    publish_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='contents_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='contents_updated')

    def __str__(self):
        return self.title

class BlogPostContent(models.Model):
    content = models.OneToOneField(Content, on_delete=models.CASCADE, related_name='blog_post_content')
    body = models.TextField()
    reading_time_minutes = models.IntegerField()
    likes = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
    author = models.CharField(max_length=255)

    def __str__(self):
        return f"Blog Post Content for {self.content.title}"
    
class VideoContent(models.Model):
    content = models.OneToOneField(Content, on_delete=models.CASCADE, related_name='video_content')
    video_url = models.URLField()
    duration_seconds = models.IntegerField()
    # views = models.IntegerField(default=0)
    # likes = models.IntegerField(default=0)
    # shares = models.IntegerField(default=0)

    def __str__(self):
        return f"Video Content for {self.content.title}"
    
class MediaAsset(models.Model):
    ASSET_TYPE_CHOICES = [
        ('image', 'Image'),
        ('video', 'Video'),
        ('audio', 'Audio'),
        ('document', 'Document'),
    ]
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='media_assets')
    asset_type = models.CharField(max_length=20, choices=ASSET_TYPE_CHOICES)
    file_url = models.URLField()
    description = models.TextField(null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='media_assets_uploaded')

    def __str__(self):
        return f"{self.asset_type} for {self.content.title}"

class ContentTag(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='content_tags')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='tagged_contents')

    def __str__(self):
        return f"Tag {self.tag.name} for {self.content.title}"

class SocialChannel(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name='channel_contents')
    account_handle = models.CharField(max_length=255)
    access_token = models.CharField(max_length=500)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"Channel {self.channel.name} for {self.content.title}"

class SocialPost(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('posted', 'Posted'),
        ('failed', 'Failed'),
    ]
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='social_posts')
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='social_channels')
    property = models.ForeignKey(Property, on_delete=models.SET_NULL, null=True, blank=True, related_name='social_posts')
    social_channel = models.ForeignKey(SocialChannel, on_delete=models.CASCADE, related_name='contents')
    caption = models.TextField()
    scheduled_post_time = models.DateTimeField(null=True, blank=True)
    posted_at = models.DateTimeField(null=True, blank=True)
    post_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"Social Channel {self.social_channel.channel.name} for {self.content.title}"
    
class SocialPostLog(models.Model):
    social_post = models.ForeignKey(SocialPost, on_delete=models.CASCADE, related_name='logs')
    status = models.CharField(max_length=20, choices=SocialPost.STATUS_CHOICES)
    error_message = models.TextField(null=True, blank=True)
    response_data = models.TextField(null=True, blank=True) 
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Log for {self.social_post} at {self.timestamp}"
    
#Email Marketing Models

class Subscriber(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('unsubscribed', 'Unsubscribed'),
        ('bounced', 'Bounced'),
    ]
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    unsubscribed_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email

class SubscriberPreference(models.Model):
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE, related_name='preferences')
    preference_location = models.CharField(max_length=100)
    preference_property_type = models.ForeignKey(PropertyType, on_delete=models.SET_NULL, null=True, blank=True, related_name='subscriber_preferences')

    def __str__(self):
        return f"Preference {self.preference_location} for {self.subscriber.email}"
    
class Newsletter(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('scheduled', 'Scheduled'),
        ('sent', 'Sent'),
        ('cancelled', 'Cancelled'),
    ]
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='newsletters')
    subject = models.CharField(max_length=255)
    content = models.TextField()
    scheduled_send_time = models.DateTimeField(null=True, blank=True)
    sent_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='newsletter_campaigns_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='newsletter_campaigns_updated')

    def __str__(self):
        return self.subject
    
class NewsletterLog(models.Model):
    STATUS_CHOICES = [
        ('sent', 'Sent'),
        ('opened', 'Opened'),
        ('bounced', 'Bounced'),
    ]
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE, related_name='logs')
    sent_to = models.EmailField()
    status = models.CharField(max_length=20, choices=Newsletter.STATUS_CHOICES)
    error_message = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Log for {self.newsletter.subject} to {self.sent_to} at {self.timestamp}"
    
# In-person Engagement Event Models
    
class EngagementEvent(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='engagement_events')     
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    event_date = models.DateField()
    attendees_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='engagement_events_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='engagement_events_updated')
    def __str__(self):
        return self.name

class EngagementAttendee(models.Model):
    event = models.ForeignKey(EngagementEvent, on_delete=models.CASCADE, related_name='attendees')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    rsvp_status = models.CharField(max_length=50)
    attended = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} attending {self.event.name}"

class EngagementFeedback(models.Model):
    event = models.ForeignKey(EngagementEvent, on_delete=models.CASCADE, related_name='feedbacks')
    attendee = models.ForeignKey(EngagementAttendee, on_delete=models.CASCADE, related_name='feedbacks')
    rating = models.IntegerField()
    comments = models.TextField(null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback by {self.attendee.name} for {self.event.name}"

# Content and Campaign Performance Metrics

class ContentPerformanceSnapshot(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='performance_metrics')
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    recorded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.metric_name} for {self.content.title} at {self.recorded_at}"
    
class CampaignContentPerformance(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='content_performance_metrics')
    impressions = models.IntegerField(default=0)
    leads_generated = models.IntegerField(default=0)
    conversions = models.IntegerField(default=0)
    recorded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Performance for {self.content.title} in {self.campaign.name} at {self.recorded_at}"
    