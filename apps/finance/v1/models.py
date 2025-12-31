from django.db import models
from apps.mediaAndMarketing.v1.models import Campaign
from apps.sales.v1.models import SalesCase
from apps.users.v1.models import User

# Create your models here.
class Revenue(models.Model):
    REVENUE_TYPE_CHOICES = [
        ('commission', 'Commission'),
        ('referralFee', 'Referral Fee')
    ]
    STATUS_CHOICES = [
        ('expected', 'Expected'),
        ('invoiced', 'Invoiced'),
        ('received', 'Received'),
        ('canceled', 'Canceled'),
    ]
    PAYMENT_CHOICES = [
        ('mpesa', 'Mpesa'),
        ('bank', 'Bank')
    ]
    sales_case = models.ForeignKey(SalesCase, on_delete=models.CASCADE, related_name='sales case')
    revenue_type = models.CharField(max_length=30, choices=REVENUE_TYPE_CHOICES, default='commission')
    amount = models.DecimalField()
    currency = models.CharField(max_length=10, default='KSH')
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='expected')
    reference_number = models.CharField(max_length=100)
    received_at  = models.DateTimeField()
    created_at = models.DateField(auto_created=True)
    updated_by = models.ForeignKey(User, related_name='updated by')
    updated_at = models.DateTimeField(auto_created=True)

    def __str__(self):
        return 'revenue of ' + self.amount +'amount'

class Expense(models.Model):
    EXPENSE_TYPE_CHOICE = [
        ('marketing', 'Marketing'),
        ('transport', 'Transport'),
        ('legal', 'Legal'),
        ('site_visit', 'Site Visit'),
        ('operations', 'operations'),
        ('salaries', 'Salaries')
    ]
    PAYMENT_METHOD_CHOICE = [
        ('mpesa', 'Mpesa'),
        ('cash', 'Cash'),
        ('bank', 'Bank'), 
    ]
    expense_type = models.CharField(max_length=30, choices=EXPENSE_TYPE_CHOICE)
    payment_method = models.CharField(max_length=30, choices=PAYMENT_METHOD_CHOICE)
    amount = models.DecimalField()
    related_sale = models.ForeignKey(SalesCase, related_name='sales case')
    related_campaign = models.ForeignKey(Campaign, related_name='campaign')
    paid_to = models.ForeignKey(User, related_name='paid to')
    transaction_ref = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_created=True)
    created_by = models.ForeignKey(User, related_name='created by')
    notes = models.TextField()

    def __str__(self):
        return 'Expense of' + self.amount + ' made to'
