from rest_framework import serializers
from .models import Revenue, Expense


class RevenueSerializer(serializers.ModelSerializer):
    sales_case_id = serializers.IntegerField(source='sales_case.id', read_only=True)
    updated_by_id = serializers.IntegerField(source='updated_by.id', read_only=True)

    class Meta:
        model = Revenue
        fields = "__all__"


class RevenueCreateSerializer(serializers.ModelSerializer):
    updated_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Revenue
        fields = [
            'sales_case',
            'revenue_type',
            'amount',
            'currency',
            'status',
            'reference_number',
            'received_at',
            'updated_by',
        ]

class ExpenseSerializer(serializers.ModelSerializer):
    related_sale_id = serializers.IntegerField(source='related_sale.id', read_only=True)
    related_campaign_id = serializers.IntegerField(source='related_campaign.id', read_only=True)
    paid_to_id = serializers.IntegerField(source='paid_to.id', read_only=True)
    created_by_id = serializers.IntegerField(source='created_by.id', read_only=True)

    class Meta:
        model = Expense
        fields = "__all__"

class ExpenseCreateSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Expense
        fields = [
            'expense_type',
            'payment_method',
            'amount',
            'related_sale',
            'related_campaign',
            'paid_to',
            'transaction_ref',
            'notes',
            'created_by'
        ]
