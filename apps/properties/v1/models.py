from django.db import models
from apps.core.v1.models import PropertyType, PropertyUse, Channel, RelationshipStatus
from apps.users.v1.models import User

# Create your models here.
#TODO title number to ensure only unique properties are added 
#  example( marmanet/ north rumuruti block 2/ 8419 (Ndurumo))

class Property(models.Model):
    PROPERTY_TYPE_CHOICES =[
        ('homes', 'Homes'),
        ('apartments', 'Apartments'),
        ('plots', 'Plots'),
        ('ranches', 'Ranches')
    ]
    PROPERTY_MODE_CHOICES = [
        ('single', 'Single'),
        ('project', 'Project'),
        ('offPlan', 'Off Plan'),
    ]

    PROPERTY_STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('available', 'Available'),
        ('underOffer', 'Under Offer'),
        ('pendingMedia', 'Pending Media'),
        ('sold', 'Sold'),
        ('archived', 'Archived'),
    ]

    TITLE_TYPE_CHOICES = [
        ('freehold', 'Freehold'),
        ('leasehold', 'Leasehold'),
    ]

    TITLE_STATUS_CHOICES = [
        ('ready', 'Ready'),
        ('processing', 'Processing'),
        ('pendingSubdivision', 'Pending Subdivision'),
        ('leaseRegistered', 'Lease Registered'),
    ]
    title_number = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE)
    property_use = models.ForeignKey(PropertyUse, on_delete=models.SET_NULL, null=True)
    property_mode = models.CharField(max_length=20, choices=PROPERTY_MODE_CHOICES)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    negotiable = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    property_status = models.CharField(max_length=50, choices=PROPERTY_STATUS_CHOICES, default='draft')
    title_status = models.CharField(max_length=100, choices=TITLE_STATUS_CHOICES, default='ready')
    title_type = models.CharField(max_length=50, choices=TITLE_TYPE_CHOICES, default='freehold')
    listed_date = models.DateTimeField(auto_now_add=True)
    is_available = models.BooleanField(default=True)
    listed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='listed_properties')

    def __str__(self):
        return self.title

# like parking, wifi, cctv
class Feature(models.Model):
    name = models.CharField(max_length=100, unique=True)
    icon  = models.URLField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    

# like church market
class Amenity(models.Model):
    name = models.CharField(max_length=100, unique=True)
    icon  = models.URLField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class PropertyAmenities(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='property_amenities')
    amenity = models.ForeignKey(Amenity, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.amenity.name}"
    
class PropertyFeatures(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='property_features')
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)
    count = models.IntegerField()

    def __str__(self):
        return f"{self.feature.name}: {self.feature.count}"

class PropertyLocation(models.Model):
    property = models.OneToOneField(Property, on_delete=models.CASCADE, related_name='location')
    address = models.TextField()
    country = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    local_area = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    location_pin = models.URLField(blank=True, null=True)


    def __str__(self):
        return self.address

class PropertyMedia(models.Model):
    MEDIA_TYPE_CHOICES = [
        ('image', 'Image'),
        ('video', 'Video'),
        ('document', 'Document'),
    ]

    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='media')
    media_type = models.CharField(max_length=20, choices=MEDIA_TYPE_CHOICES)
    url = models.URLField()
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_cover = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.media_type} for {self.property.title}"

class Land(models.Model):
    property = models.OneToOneField(Property, on_delete=models.CASCADE, related_name='land_details')
    plot_size = models.DecimalField(max_digits=10, decimal_places=2)
    zoning_information = models.TextField(blank=True, null=True)
    soil_type = models.CharField(max_length=100, blank=True, null=True)
    topography = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Land details for {self.property.title}"
    
class Building(models.Model):
    CONSTRUCTION_STATUS_CHOICES = [
        ('planned', 'Planned'),
        ('underConstruction', 'Under Construction'),
        ('completed', 'Completed'),
        ('renovation', 'Renovation'),
    ]
    property = models.OneToOneField(Property, on_delete=models.CASCADE, related_name='building_details')
    built_up_area = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_floors = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    parking_spaces = models.IntegerField()
    year_built = models.IntegerField(blank=True, null=True)
    construction_status = models.CharField(max_length=100, choices=CONSTRUCTION_STATUS_CHOICES)

    def __str__(self):
        return f"Building details for {self.property.title}"
    
class Project(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='projects')
    total_units = models.IntegerField()
    ongoing_units = models.IntegerField(default=0)
    available_units = models.IntegerField(default=0)
    # description = models.TextField()
    start_date = models.DateField()
    expected_completion_date = models.DateField()
    actual_completion_date = models.DateField(blank=True, null=True)
    payment_plans_availability = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class ProjectUnit(models.Model):
    UNIT_STATUS_CHOICES = [
        ('available', 'Available'),
        ('sold', 'Sold'),
        ('reserved', 'Reserved'),
        ('underOffer', 'Under Offer'),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='units')
    unit_number = models.CharField(max_length=100)
    floor_number = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    built_up_area = models.DecimalField(max_digits=10, decimal_places=2)
    measurement_unit = models.CharField(max_length=50)  # e.g., square feet, square meters
    price = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=50, choices=UNIT_STATUS_CHOICES, default='available')

    def __str__(self):
        return f"Unit {self.unit_number} in {self.project.name}"

class BookmarkedProperty(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookmarks')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='bookmarked_by')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.user.first_name} bookmarked {self.property.title}"
    