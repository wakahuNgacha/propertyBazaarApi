from rest_framework import serializers
from .models import Appointment, AppointmentParticipant
from apps.users.v1.serializers import UserSerializer
from apps.sales.v1.serializers import SalesCaseSerializer

class AppointmentParticipantSerializer(serializers.ModelSerializer):
    participant = UserSerializer(read_only=True)

    class Meta:
        model = AppointmentParticipant
        fields = "__all__"

class AppointmentParticipantCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentParticipant
        fields = [
            'appointment',
            'participant',
            'participant_name',
            'participant_phone',
            'participant_email'
        ]


class AppointmentSerializer(serializers.ModelSerializer):
    assigned_to = UserSerializer(read_only=True)
    created_by = UserSerializer(read_only=True)
    sales_case = SalesCaseSerializer(read_only=True)
    participants = AppointmentParticipantSerializer(
        source='Appointment',
        many=True,
        read_only=True
    )

    class Meta:
        model = Appointment
        fields = "__all__"

class AppointmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = [
            'appointment_type',
            'title',
            'sales_case',
            'scheduled_at',
            'scheduled_end',
            'location',
            'assigned_to',
            'status',
            'outcome',
            'notes'
        ]

class AppointmentCreateWithParticipantsSerializer(serializers.ModelSerializer):
    participants = AppointmentParticipantCreateSerializer(many=True)

    class Meta:
        model = Appointment
        fields = [
            'appointment_type',
            'title',
            'sales_case',
            'scheduled_at',
            'scheduled_end',
            'location',
            'assigned_to',
            'status',
            'outcome',
            'notes',
            'participants'
        ]

    def create(self, validated_data):
        participants_data = validated_data.pop('participants')
        appointment = Appointment.objects.create(**validated_data)

        for participant in participants_data:
            AppointmentParticipant.objects.create(
                appointment=appointment,
                **participant
            )

        return appointment
