from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView
)
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import *
from .serializers import *

# Create your views here.
class LeadListView(ListAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permission_classes = [IsAuthenticated]


class LeadCreateView(CreateAPIView):
    serializer_class = LeadCreateSerializer
    permission_classes = [IsAuthenticated]


class LeadDetailView(RetrieveAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    lookup_field = "id"
    permission_classes = [IsAuthenticated]


class LeadUpdateView(UpdateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadCreateSerializer
    lookup_field = "id"
    permission_classes = [IsAuthenticated]

class InquiryListView(ListAPIView):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer
    permission_classes = [IsAuthenticated]


class InquiryCreateView(CreateAPIView):
    serializer_class = InquiryCreateSerializer
    permission_classes = [IsAuthenticated]


class InquiryDetailView(RetrieveAPIView):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer
    lookup_field = "id"
    permission_classes = [IsAuthenticated]


class InquiryUpdateView(UpdateAPIView):
    queryset = Inquiry.objects.all()
    serializer_class = InquiryCreateSerializer
    lookup_field = "id"
    permission_classes = [IsAuthenticated]

class SalesCaseListView(ListAPIView):
    queryset = SalesCase.objects.all()
    serializer_class = SalesCaseSerializer
    permission_classes = [IsAuthenticated]


class SalesCaseCreateView(CreateAPIView):
    serializer_class = SalesCaseCreateSerializer
    permission_classes = [IsAuthenticated]


class SalesCaseDetailView(RetrieveAPIView):
    queryset = SalesCase.objects.all()
    serializer_class = SalesCaseSerializer
    lookup_field = "id"
    permission_classes = [IsAuthenticated]


class SalesCaseUpdateView(UpdateAPIView):
    queryset = SalesCase.objects.all()
    serializer_class = SalesCaseCreateSerializer
    lookup_field = "id"
    permission_classes = [IsAuthenticated]

class FollowUpListView(ListAPIView):
    queryset = FollowUp.objects.all()
    serializer_class = FollowUpSerializer
    permission_classes = [IsAuthenticated]


class FollowUpCreateView(CreateAPIView):
    serializer_class = FollowUpCreateSerializer
    permission_classes = [IsAuthenticated]


class FollowUpDetailView(RetrieveAPIView):
    queryset = FollowUp.objects.all()
    serializer_class = FollowUpSerializer
    lookup_field = "id"
    permission_classes = [IsAuthenticated]


class FollowUpUpdateView(UpdateAPIView):
    queryset = FollowUp.objects.all()
    serializer_class = FollowUpCreateSerializer
    lookup_field = "id"
    permission_classes = [IsAuthenticated]

class OfferListView(ListAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [IsAuthenticated]


class OfferCreateView(CreateAPIView):
    serializer_class = OfferCreateSerializer
    permission_classes = [IsAuthenticated]


class OfferDetailView(RetrieveAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    lookup_field = "id"
    permission_classes = [IsAuthenticated]


class OfferUpdateView(UpdateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferCreateSerializer
    lookup_field = "id"
    permission_classes = [IsAuthenticated]

class ReferralListView(ListAPIView):
    queryset = Referral.objects.all()
    serializer_class = ReferralSerializer
    permission_classes = [IsAuthenticated]


class ReferralCreateView(CreateAPIView):
    serializer_class = ReferralCreateSerializer
    permission_classes = [IsAuthenticated]


class ReferralDetailView(RetrieveAPIView):
    queryset = Referral.objects.all()
    serializer_class = ReferralSerializer
    lookup_field = "id"
    permission_classes = [IsAuthenticated]


class ReferralUpdateView(UpdateAPIView):
    queryset = Referral.objects.all()
    serializer_class = ReferralCreateSerializer
    lookup_field = "id"
    permission_classes = [IsAuthenticated]

class SaleClosureListView(ListAPIView):
    queryset = SaleClosure.objects.all()
    serializer_class = SaleClosureSerializer
    permission_classes = [IsAuthenticated]


class SaleClosureCreateView(CreateAPIView):
    serializer_class = SaleClosureCreateSerializer
    permission_classes = [IsAuthenticated]


class SaleClosureDetailView(RetrieveAPIView):
    queryset = SaleClosure.objects.all()
    serializer_class = SaleClosureSerializer
    lookup_field = "id"
    permission_classes = [IsAuthenticated]


class SaleClosureUpdateView(UpdateAPIView):
    queryset = SaleClosure.objects.all()
    serializer_class = SaleClosureCreateSerializer
    lookup_field = "id"
    permission_classes = [IsAuthenticated]

class PostSaleTaskListView(ListAPIView):
    queryset = PostSaleTask.objects.all()
    serializer_class = PostSaleTaskSerializer
    permission_classes = [IsAuthenticated]


class PostSaleTaskCreateView(CreateAPIView):
    serializer_class = PostSaleTaskCreateSerializer
    permission_classes = [IsAuthenticated]


class PostSaleTaskDetailView(RetrieveAPIView):
    queryset = PostSaleTask.objects.all()
    serializer_class = PostSaleTaskSerializer
    lookup_field = "id"
    permission_classes = [IsAuthenticated]


class PostSaleTaskUpdateView(UpdateAPIView):
    queryset = PostSaleTask.objects.all()
    serializer_class = PostSaleTaskCreateSerializer
    lookup_field = "id"
    permission_classes = [IsAuthenticated]
