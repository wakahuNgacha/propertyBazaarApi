from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView
)
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Revenue, Expense
from .serializers import (
    RevenueSerializer,
    RevenueCreateSerializer,
    ExpenseSerializer,
    ExpenseCreateSerializer
)

# Create your views here.
class RevenueListView(ListAPIView):
    queryset = Revenue.objects.all().order_by('-created_at')
    serializer_class = RevenueSerializer
    permission_classes = [IsAuthenticated]

class RevenueCreateView(CreateAPIView):
    queryset = Revenue.objects.all()
    serializer_class = RevenueCreateSerializer
    permission_classes = [IsAuthenticated]

class RevenueDetailView(RetrieveAPIView):
    queryset = Revenue.objects.all()
    serializer_class = RevenueSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

class RevenueUpdateView(UpdateAPIView):
    queryset = Revenue.objects.all()
    serializer_class = RevenueCreateSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

class ExpenseListView(ListAPIView):
    queryset = Expense.objects.all().order_by('-created_at')
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

class ExpenseCreateView(CreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseCreateSerializer
    permission_classes = [IsAuthenticated]

class ExpenseDetailView(RetrieveAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

class ExpenseUpdateView(UpdateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseCreateSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]
