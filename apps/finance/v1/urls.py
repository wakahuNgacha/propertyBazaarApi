from django.urls import path
from .views import *

urlpatterns = [

    # REVENUE
    path("revenue/", RevenueListView.as_view()),
    path("revenue/create/", RevenueCreateView.as_view()),
    path("revenue/<int:id>/", RevenueDetailView.as_view()),
    path("revenue/<int:id>/update/", RevenueUpdateView.as_view()),

    # EXPENSES
    path("expenses/", ExpenseListView.as_view()),
    path("expenses/create/", ExpenseCreateView.as_view()),
    path("expenses/<int:id>/", ExpenseDetailView.as_view()),
    path("expenses/<int:id>/update/", ExpenseUpdateView.as_view()),
]
