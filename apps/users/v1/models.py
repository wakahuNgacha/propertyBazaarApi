from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from apps.core.v1.models import PropertyType, PropertyUse, Channel, RelationshipStatus

# Create your models here.

class User(models.Model):
    # same page
    # Admin page: admin, finance, sales 
    # BUyer: buyer, owner, ReferralAgent
    # Broker: broker
    # Partner: partner
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('buyer', 'Buyer'),
        ('broker', 'Broker'),
        ('owner','Owner'),
        ('referralAgent','Referral Agent'),
        ('partner','Partner'),
        ('finance','Finance'),
        ('SalesAndMarketing','Sales And Marketing'),
    ]

    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    last_active_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return self.email
    
class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clients')
    preferred_property_type = models.ForeignKey(PropertyType, on_delete=models.SET_NULL, null=True)
    preferred_use = models.ForeignKey(PropertyUse, on_delete=models.SET_NULL, null=True)
    preferred_channel = models.ForeignKey(Channel, on_delete=models.SET_NULL, null=True)
    relationship_status = models.ForeignKey(RelationshipStatus, on_delete=models.SET_NULL, null=True)
    location_preferences = models.TextField()    
    budget_range = models.CharField(max_length=50)
    urgency_level = models.CharField(max_length=50)
    min_land_size = models.FloatField()
    max_land_size = models.FloatField()
    house_size = models.FloatField()
    house_bedrooms_min = models.IntegerField()
    house_bedrooms_max = models.IntegerField()
    house_bathrooms_min = models.IntegerField()
    house_bathrooms_max = models.IntegerField()
    conversion_stage = models.CharField(max_length=50)
    source_of_lead = models.CharField(max_length=100)
    last_contacted = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.first_name
    
class Broker(models.Model):
    BROKER_TYPE_CHOICES = [
        ('independent', 'Independent'),
        ('agency', 'Agency'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='brokers')
    license_number = models.CharField(max_length=50, unique=True)
    broker_type = models.CharField(max_length=50, choices=BROKER_TYPE_CHOICES)
    years_of_experience = models.IntegerField()
    areas_of_expertise = models.TextField()
    primary_location = models.CharField(max_length=100)
    service_areas = models.TextField()
    bio = models.TextField()
    relationship_status = models.ForeignKey(RelationshipStatus, on_delete=models.SET_NULL, null=True)
    verified = models.BooleanField(default=False)
    active_listings = models.IntegerField(default=0)
    total_listings = models.IntegerField(default=0)
    total_sales = models.IntegerField(default=0)
    rating = models.FloatField(default=0.0)
    profile_picture = models.URLField(blank=True, null=True)
    id_document = models.URLField(blank=True, null=True)
    kra_documents = models.URLField(blank=True, null=True)
    agreement_signed = models.BooleanField(default=False)
    agreement_document = models.URLField(blank=True, null=True)
    verified_at = models.DateTimeField(null=True, blank=True)
    verified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='verified_brokers')
    public_slug = models.SlugField(unique=True)



    def __str__(self):
        return self.user.first_name

class Owner(models.Model):
    OWNER_TYPE_CHOICES = [
        ('individual', 'Individual'),
        ('company', 'Company'), 
        # also developer
    ]
    owner_type = models.CharField(max_length=50, choices=OWNER_TYPE_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owners')
    relationship_status = models.ForeignKey(RelationshipStatus, on_delete=models.SET_NULL, null=True)
    total_properties = models.IntegerField(default=0)
    active_properties = models.IntegerField(default=0)
    sold_properties = models.IntegerField(default=0)
    verified = models.BooleanField(default=False)
    verified_at = models.DateTimeField(null=True, blank=True)
    verified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='verified_owners')


    def __str__(self):
        return self.user.first_name
    
class Company(models.Model):
    Owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='companies')
    registration_number = models.CharField(max_length=50, unique=True)
    address = models.TextField()
    property_types = models.ManyToManyField(PropertyType, related_name='companies')
    website = models.URLField(blank=True, null=True)
    profile_description = models.TextField(blank=True, null=True)
    profile_picture = models.URLField(blank=True, null=True)
    project_count= models.IntegerField(default=0)
    completed_projects = models.IntegerField(default=0)
    ongoing_projects = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Partner(models.Model):
    PARTNER_TYPE_CHOICES = [
        ('legal', 'Legal'),
        ('inspection', 'Inspection'),
        ('valuation', 'Valuation'),
        ('other', 'Other'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='partners')
    partner_type = models.CharField(max_length=50, choices=PARTNER_TYPE_CHOICES)
    company_name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)
    address = models.TextField()
    services_offered = models.TextField()
    rating = models.FloatField(default=0.0)
    verified = models.BooleanField(default=False)
    verified_at = models.DateTimeField(null=True, blank=True)
    verified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='verified_partners')

    def __str__(self):
        return self.company_name
    
class ReferralAgent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='referral_agents')
    agency_name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)
    address = models.TextField()
    total_referrals = models.IntegerField(default=0)
    successful_referrals = models.IntegerField(default=0)
    rating = models.FloatField(default=0.0)
    verified = models.BooleanField(default=False)
    verified_at = models.DateTimeField(null=True, blank=True)
    verified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='verified_referral_agents')

    def __str__(self):
        return self.agency_name
    
class Admin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admins')
    role_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.first_name

class Staff(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='staff_members')
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.user.first_name
    