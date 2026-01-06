from django.urls import path
from .views import *

urlpatterns = [
    path("users/", UserListView.as_view()),
    path("users/create/", UserCreateView.as_view()),
    path("users/<int:user_id>/", UserDetailView.as_view()),
    path("users/<int:user_id>/update/", UserUpdateView.as_view()),

    path("clients/", ClientListView.as_view()),
    path("clients/create/", ClientCreateView.as_view()),
    path("clients/<int:client_id>/", ClientDetailView.as_view()),
    path("clients/<int:client_id>/update/", ClientUpdateView.as_view()),

    path("brokers/", BrokerListView.as_view()),
    path("brokers/create/", BrokerCreateView.as_view()),
    path("brokers/<int:broker_id>/", BrokerDetailView.as_view()),
    path("brokers/<int:broker_id>/update/", BrokerUpdateView.as_view()),

    path("owners/", OwnerListView.as_view()),
    path("owners/create/", OwnerCreateView.as_view()),
    path("owners/<int:owner_id>/", OwnerDetailView.as_view()),
    path("owners/<int:owner_id>/update/", OwnerUpdateView.as_view()),

    path("companies/", CompanyListView.as_view()),
    path("companies/create/", CompanyCreateView.as_view()),
    path("companies/<int:company_id>/", CompanyDetailView.as_view()),
    path("companies/<int:company_id>/update/", CompanyUpdateView.as_view()),

    path("partners/", PartnerListView.as_view()),
    path("partners/create/", PartnerCreateView.as_view()),
    path("partners/<int:partner_id>/", PartnerDetailView.as_view()),
    path("partners/<int:partner_id>/update/", PartnerUpdateView.as_view()),

    path("referral-agents/", ReferralAgentListView.as_view()),
    path("referral-agents/create/", ReferralAgentCreateView.as_view()),
    path("referral-agents/<int:agent_id>/", ReferralAgentDetailView.as_view()),
    path("referral-agents/<int:agent_id>/update/", ReferralAgentUpdateView.as_view()),

    path("staff/", StaffListView.as_view()),
    path("staff/create/", StaffCreateView.as_view()),
    path("staff/<int:staff_id>/", StaffDetailView.as_view()),
    path("staff/<int:staff_id>/update/", StaffUpdateView.as_view()),

    path("admins/", AdminListView.as_view()),
    path("admins/create/", AdminCreateView.as_view()),
    path("admins/<int:admin_id>/", AdminDetailView.as_view()),
    path("admins/<int:admin_id>/update/", AdminUpdateView.as_view()),
]
