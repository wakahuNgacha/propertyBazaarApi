from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from rest_framework.permissions import IsAuthenticated

from .models import Appointment, AppointmentParticipant
from .serializers import (
    AppointmentSerializer,
    AppointmentCreateSerializer,
    AppointmentParticipantSerializer,
    AppointmentParticipantCreateSerializer
)


# Create your views here.
class AppointmentListView(ListAPIView):
    queryset = Appointment.objects.all().order_by('-scheduled_at')
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

class AppointmentCreateView(CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class AppointmentDetailView(RetrieveAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

class AppointmentUpdateView(UpdateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentCreateSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

class AppointmentDeleteView(DestroyAPIView):
    queryset = Appointment.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

class AppointmentParticipantListView(ListAPIView):
    serializer_class = AppointmentParticipantSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        appointment_id = self.kwargs['appointment_id']
        return AppointmentParticipant.objects.filter(
            appointment_id=appointment_id
        )

class AppointmentParticipantCreateView(CreateAPIView):
    queryset = AppointmentParticipant.objects.all()
    serializer_class = AppointmentParticipantCreateSerializer
    permission_classes = [IsAuthenticated]

class AppointmentParticipantDeleteView(DestroyAPIView):
    queryset = AppointmentParticipant.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
