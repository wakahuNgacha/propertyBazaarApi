from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *
from .serializers import *


# Create your views here.
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            return Response({
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh),
                'user': AuthUserSerializer(user).data
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserCreateView(CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]

class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "user_id"

class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "user_id"

class ClientListView(ListAPIView):
    queryset = Client.objects.select_related("user")
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

class ClientCreateView(CreateAPIView):
    serializer_class = ClientCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ClientDetailView(RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "client_id"

class ClientUpdateView(UpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientCreateSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "client_id"

class BrokerListView(ListAPIView):
    queryset = Broker.objects.select_related("user")
    serializer_class = BrokerSerializer
    permission_classes = [IsAuthenticated]

class BrokerCreateView(CreateAPIView):
    serializer_class = BrokerCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BrokerDetailView(RetrieveAPIView):
    queryset = Broker.objects.all()
    serializer_class = BrokerSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "broker_id"

class BrokerUpdateView(UpdateAPIView):
    queryset = Broker.objects.all()
    serializer_class = BrokerCreateSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "broker_id"

class OwnerListView(ListAPIView):
    queryset = Owner.objects.select_related("user")
    serializer_class = OwnerSerializer
    permission_classes = [IsAuthenticated]

class OwnerCreateView(CreateAPIView):
    serializer_class = OwnerCreateSerializer
    permission_classes = [IsAuthenticated]

class OwnerDetailView(RetrieveAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "owner_id"

class OwnerUpdateView(UpdateAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerCreateSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "owner_id"

class CompanyListView(ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]

class CompanyCreateView(CreateAPIView):
    serializer_class = CompanyCreateSerializer
    permission_classes = [IsAuthenticated]

class CompanyDetailView(RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "company_id"

class CompanyUpdateView(UpdateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyCreateSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "company_id"

class PartnerListView(ListAPIView):
    queryset = Partner.objects.select_related("user")
    serializer_class = PartnerSerializer
    permission_classes = [IsAuthenticated]

class PartnerCreateView(CreateAPIView):
    serializer_class = PartnerCreateSerializer
    permission_classes = [IsAuthenticated]

class PartnerDetailView(RetrieveAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "partner_id"

class PartnerUpdateView(UpdateAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerCreateSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "partner_id"

class ReferralAgentListView(ListAPIView):
    queryset = ReferralAgent.objects.select_related("user")
    serializer_class = ReferralAgentSerializer
    permission_classes = [IsAuthenticated]

class ReferralAgentCreateView(CreateAPIView):
    serializer_class = ReferralAgentCreateSerializer
    permission_classes = [IsAuthenticated]

class ReferralAgentDetailView(RetrieveAPIView):
    queryset = ReferralAgent.objects.all()
    serializer_class = ReferralAgentSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "agent_id"

class ReferralAgentUpdateView(UpdateAPIView):
    queryset = ReferralAgent.objects.all()
    serializer_class = ReferralAgentCreateSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "agent_id"

class StaffListView(ListAPIView):
    queryset = Staff.objects.select_related("user")
    serializer_class = StaffSerializer
    permission_classes = [IsAuthenticated]

class StaffCreateView(CreateAPIView):
    serializer_class = StaffCreateSerializer
    permission_classes = [IsAuthenticated]

class StaffDetailView(RetrieveAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "staff_id"

class StaffUpdateView(UpdateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffCreateSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "staff_id"

class AdminListView(ListAPIView):
    queryset = Admin.objects.select_related("user")
    serializer_class = AdminSerializer
    permission_classes = [IsAuthenticated]

class AdminCreateView(CreateAPIView):
    serializer_class = AdminCreateSerializer
    permission_classes = [IsAuthenticated]

class AdminDetailView(RetrieveAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "admin_id"

class AdminUpdateView(UpdateAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminCreateSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "admin_id"
