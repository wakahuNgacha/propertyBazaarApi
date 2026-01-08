from django.urls import path
from .views import *

urlpatterns = [

    # LEADS
    path("leads/", LeadListView.as_view()),
    path("leads/create/", LeadCreateView.as_view()),
    path("leads/<int:id>/", LeadDetailView.as_view()),
    path("leads/<int:id>/update/", LeadUpdateView.as_view()),

    # INQUIRIES
    path("inquiries/", InquiryListView.as_view()),
    path("inquiries/create/", InquiryCreateView.as_view()),
    path("inquiries/<int:id>/", InquiryDetailView.as_view()),
    path("inquiries/<int:id>/update/", InquiryUpdateView.as_view()),

    # SALES CASES
    path("sales-cases/", SalesCaseListView.as_view()),
    path("sales-cases/create/", SalesCaseCreateView.as_view()),
    path("sales-cases/<int:id>/", SalesCaseDetailView.as_view()),
    path("sales-cases/<int:id>/update/", SalesCaseUpdateView.as_view()),

    # FOLLOW UPS
    path("follow-ups/", FollowUpListView.as_view()),
    path("follow-ups/create/", FollowUpCreateView.as_view()),
    path("follow-ups/<int:id>/", FollowUpDetailView.as_view()),
    path("follow-ups/<int:id>/update/", FollowUpUpdateView.as_view()),

    # OFFERS
    path("offers/", OfferListView.as_view()),
    path("offers/create/", OfferCreateView.as_view()),
    path("offers/<int:id>/", OfferDetailView.as_view()),
    path("offers/<int:id>/update/", OfferUpdateView.as_view()),

    # REFERRALS
    path("referrals/", ReferralListView.as_view()),
    path("referrals/create/", ReferralCreateView.as_view()),
    path("referrals/<int:id>/", ReferralDetailView.as_view()),
    path("referrals/<int:id>/update/", ReferralUpdateView.as_view()),

    # SALE CLOSURES
    path("sale-closures/", SaleClosureListView.as_view()),
    path("sale-closures/create/", SaleClosureCreateView.as_view()),
    path("sale-closures/<int:id>/", SaleClosureDetailView.as_view()),
    path("sale-closures/<int:id>/update/", SaleClosureUpdateView.as_view()),

    # POST SALE TASKS
    path("post-sale-tasks/", PostSaleTaskListView.as_view()),
    path("post-sale-tasks/create/", PostSaleTaskCreateView.as_view()),
    path("post-sale-tasks/<int:id>/", PostSaleTaskDetailView.as_view()),
    path("post-sale-tasks/<int:id>/update/", PostSaleTaskUpdateView.as_view()),
]
