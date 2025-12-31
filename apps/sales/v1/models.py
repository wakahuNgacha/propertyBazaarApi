from django.db import models
from apps.properties.v1.models import Property
from apps.core.v1.models import Channel, PropertyType
from apps.users.v1.models import User

# Create your models here.
class Lead(models.Model):
    LEAD_TYPE_CHOICES = [
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
        ('developer', 'Developer')

    ]
    STATUS_CHOICES =[
        ('new', 'New'),
        ('contacted', 'Contacted'),
        ('qualified', 'Qualified'),
        ('disqualified', 'Disqualified' )
    ]
    client_name = models.CharField(max_length=30)
    client_phone = models.CharField(max_length=15, unique=True)
    client_email = models.EmailField()
    lead_type = models.CharField(max_length=30)
    source = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name='channel')
    preferred_location = models.CharField()
    preferred_property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE, related_name='property type')
    budget_min = models.DecimalField(max_digits=10, decimal_places=2)
    budget_max = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='assigned_to')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.client_name
    

class Inquiry(models.Model):
    INQUIRY_TYPE_CHOICES = [
        ('buy', 'Buy'),
        ('lease', 'Lease'),
        ('siteVisit', 'Site Visit')
    ]

    URGENCY_LEVEL_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    STATUS_CHOICES = [
        ('open', 'Open'),
        ('schedule', 'Schedule'),
        ('converted', 'Converted'),
        ('closed', 'Closed')
    ]
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name='lead' )
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='property')
    inquiry_type = models.CharField(max_length=20, choices= INQUIRY_TYPE_CHOICES)
    message = models.TextField()
    urgency_level = models.CharField(max_length=20, choices= URGENCY_LEVEL_CHOICES)
    status = models.CharField(max_length= 20, choices=STATUS_CHOICES)
    created_at =  models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.lead.client_name

class SalesCase (models.Model):
    STAGE_CHOICES = [
        ('new', 'New'),
        ('siteVisitDone', 'Site visit Done'),
        ('negotiations', 'Negotiations'),
        ('offerMade', 'Offer Made'),
        ('dueDiligence', 'Due Diligence'),
        ('contractSigned', 'Contract Signed'),
        ('closedWon', 'Closed Won'),
        ('closedLost', 'Closed Lost'),
    ]
    inquiry = models.ForeignKey(Inquiry, on_delete=models.CASCADE, related_name='inquiry')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='property')
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='buyer')
    from_lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name='lead')
    assigned_to = models.ForeignKey(User)
    stage = models.CharField(max_length=20, choices=STAGE_CHOICES, default='new')
    expected_price = models.DecimalField(max_digits=10, decimal_places=2)
    agreed_price = models.DecimalField(max_digits=10, decimal_places=2)
    expected_commission = models.DecimalField(max_digits=10, decimal_places=2)
    actual_commission = models.DecimalField(max_digits=10, decimal_places=2)
    closing_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created by')

    def __str__(self):
        return 'created by' + self.created_by + 'inquired by' + self.buyer
    
class FollowUp(models.Model):
    FOLLOWUP_TYPE_CHOICE = [
        ('call', 'Call'),
        ('whatsApp', 'Whats App'),
        ('email', 'Email'),
        ('meeting', 'Meeting')
    ]
    sales_case = models.ForeignKey(SalesCase, on_delete=models.CASCADE, related_name='sales case')
    follow_up_type = models.CharField(max_length=20, choices=FOLLOWUP_TYPE_CHOICE)
    note = models.TextField()
    next_action = models.TextField()
    next_action_date = models.DateField()
    completed  = models.BooleanField()
    created_by = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)

class Offer(models.Model):
    STATUS_CHOICES = [
        ('pending', 'pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('countered', 'Countered')
    ]
    sales_case = models.ForeignKey(SalesCase, on_delete=models.CASCADE, related_name='sales case')
    made_by = models.ForeignKey(User, related_name='offer made by')
    offered_price = models.DecimalField(max_digits=10, decimal_places=2)
    offered_date = models.DateTimeField(auto_now_add=True)
    expiry_at = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    notes = models.TextField()

    def __str__(self):
        return 'offer made at' + self.offered_price

class Referral(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('payable', 'Payable'),
        ('paid', 'Paid'),
    ]
    sales_case = models.ForeignKey(SalesCase, on_delete=models.CASCADE, related_name='sales case')
    referrer_user = models.ForeignKey(User, null= True, related_name='referring')
    referrer_name = models.CharField(max_length=30)
    referrer_phone = models.CharField(max_length=10)
    referrer_email = models.EmailField(max_length=30)
    referred_client_name = models.CharField(max_length=30)
    referred_client_phone = models.CharField(max_length=10)
    referrer_client_email = models.EmailField(max_length=30)
    commission_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    paid_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'created by' + self.referrer_name
    
class SaleClosure (models.Model):
    OUTCOME_CHOICES = [
        ('won', 'Won'),
        ('lost', 'Lost'),
    ]
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('partial', 'Partial'),
        ('paid', 'Paid')
    ]
    sales_case = models.Model(SalesCase)
    closing_date = models.DateField()
    outcome = models.CharField(max_length=20, choices=OUTCOME_CHOICES)
    lose_reason = models.TextField()
    payment_status = models.CharField(max_length=30, choices=PAYMENT_STATUS_CHOICES)
    documents_completed = models.BooleanField()
    document = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User)
    updated_at = models.DateTimeField(auto_now_add=True)
    paid_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Sale closure of' + self.sales_case.property
    
class PostSaleTask (models.Model):
    TASK_TYPE_CHOICES = [
        ('titleTransfer', 'Title Transfer'),
        ('handOver', 'Hand Over'),
        ('commissionPayment', 'Commission Payment ')
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('inProgress', 'In Progress'),
        ('completed', 'Completed')
    ]
    sales_closure = models.ForeignKey(SaleClosure)
    task_type = models.CharField(max_length=30, choices=TASK_TYPE_CHOICES)
    assigned_to = models.ForeignKey(User, related_name='assignee')
    status = models.CharField(max_length=30, choices=STATUS_CHOICES)
    due_date = models.DateField()
