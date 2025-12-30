from django.db import models
from apps.properties.v1.models import Property
from apps.core.v1.models import Channel, PropertyType

# Create your models here.
class Lead(models.Model):
    LEAD_TYPE_CHOICES = [
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
        ('developer', 'Developer')

    ]
    client_name = models.CharField(max_length=30)
    client_phone = models.CharField(max_length=15, unique=True)
    client_email = models.EmailField()
    lead_type = models.CharField(max_length=30)
    source = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name='channel')
    preferred_location = models.CharField()
    preferred_property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE, related_name='property type')
    


