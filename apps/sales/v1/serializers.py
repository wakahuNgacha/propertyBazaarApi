from rest_framework import serializers
from .models import *

class LeadSerializer(serializers.ModelSerializer):
    assigned_to = serializers.StringRelatedField()

    class Meta:
        model = Lead
        fields = "__all__"

class LeadCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = [
            "client_name",
            "client_phone",
            "client_email",
            "lead_type",
            "source",
            "preferred_location",
            "preferred_property_type",
            "budget_min",
            "budget_max",
            "assigned_to",
        ]

class InquirySerializer(serializers.ModelSerializer):
    lead = LeadSerializer(read_only=True)
    property = serializers.StringRelatedField()

    class Meta:
        model = Inquiry
        fields = "__all__"

class InquiryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = [
            "lead",
            "property",
            "inquiry_type",
            "message",
            "urgency_level",
        ]

class SalesCaseSerializer(serializers.ModelSerializer):
    inquiry = InquirySerializer(read_only=True)
    property = serializers.StringRelatedField()
    buyer = serializers.StringRelatedField()
    assigned_to = serializers.StringRelatedField()

    class Meta:
        model = SalesCase
        fields = "__all__"


class SalesCaseCreateSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = SalesCase
        fields = [
            "inquiry",
            "property",
            "buyer",
            "from_lead",
            "assigned_to",
            "expected_price",
            "expected_commission",
            "closing_date",
            "created_by",
        ]

class FollowUpSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()

    class Meta:
        model = FollowUp
        fields = "__all__"

class FollowUpCreateSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = FollowUp
        fields = [
            "sales_case",
            "follow_up_type",
            "note",
            "next_action",
            "next_action_date",
            "completed",
            "created_by",
        ]


class OfferSerializer(serializers.ModelSerializer):
    made_by = serializers.StringRelatedField()

    class Meta:
        model = Offer
        fields = "__all__"

class OfferCreateSerializer(serializers.ModelSerializer):
    made_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Offer
        fields = [
            "sales_case",
            "offered_price",
            "expiry_at",
            "notes",
            "made_by",
        ]

class ReferralSerializer(serializers.ModelSerializer):
    referrer_user = serializers.StringRelatedField()

    class Meta:
        model = Referral
        fields = "__all__"


class ReferralCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referral
        fields = [
            "sales_case",
            "referrer_user",
            "referrer_name",
            "referrer_phone",
            "referrer_email",
            "referred_client_name",
            "referred_client_phone",
            "referrer_client_email",
            "commission_amount",
        ]


class SaleClosureSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleClosure
        fields = "__all__"

class SaleClosureCreateSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = SaleClosure
        fields = [
            "sales_case",
            "closing_date",
            "outcome",
            "lose_reason",
            "payment_status",
            "documents_completed",
            "document",
            "created_by",
        ]


class PostSaleTaskSerializer(serializers.ModelSerializer):
    assigned_to = serializers.StringRelatedField()

    class Meta:
        model = PostSaleTask
        fields = "__all__"


class PostSaleTaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostSaleTask
        fields = [
            "sales_closure",
            "task_type",
            "assigned_to",
            "status",
            "due_date",
        ]
