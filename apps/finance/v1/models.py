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
    sales_case = models.ForeignKey(SalesCase, on_delete=models.CASCADE, related_name='revenue_from_sales_case')
    revenue_type = models.CharField(max_length=30, choices=REVENUE_TYPE_CHOICES, default='commission')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=10, default='KSH')
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='expected')
    reference_number = models.CharField(max_length=100)
    received_at  = models.DateTimeField()
    created_at = models.DateField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='updated_by')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Revenue {self.amount} {self.currency}"


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
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    related_sale = models.ForeignKey(SalesCase, on_delete=models.CASCADE, related_name='sales_case')
    related_campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='campaign')
    paid_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='paid_to')
    transaction_ref = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_by')
    notes = models.TextField()

    def __str__(self):
        return f"Expense of {self.amount} made to"

