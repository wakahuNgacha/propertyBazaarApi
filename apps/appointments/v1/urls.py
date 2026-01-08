from django.urls import path
from .views import *

urlpatterns = [

    # APPOINTMENTS
    path("appointments/", AppointmentListView.as_view()),
    path("appointments/create/", AppointmentCreateView.as_view()),
    path("appointments/<int:id>/", AppointmentDetailView.as_view()),
    path("appointments/<int:id>/update/", AppointmentUpdateView.as_view()),
    path("appointments/<int:id>/delete/", AppointmentDeleteView.as_view()),

    # PARTICIPANTS
    path("appointments/<int:appointment_id>/participants/", AppointmentParticipantListView.as_view()),
    path("appointment-participants/create/", AppointmentParticipantCreateView.as_view()),
    path("appointment-participants/<int:id>/delete/", AppointmentParticipantDeleteView.as_view()),
]
