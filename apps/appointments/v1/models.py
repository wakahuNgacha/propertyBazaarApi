from django.db import models
from apps.sales.v1.models import SalesCase
from apps.users.v1.models import User

# Create your models here.
class Appointment(models.Model):
    APPOINTMENT_TYPE_CHOICES = [
        ('siteVisit', 'Site Visit'),
        ('landSearch', 'Land search'),
        ('dealClosing', 'Deal Closing'),
        ('inspection', 'Inspection'),
        ('meeting', 'Meeting'),
        ('call', 'Call'),
        ('virtualTour', 'Virtual Tour'),
    ]
    STATUS_CHOICE = [
        ('scheduled', 'Scheduled'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('canceled', 'Cancelled'),
        ('rescheduled', 'Rescheduled'),
        ('noShow', 'No Show')
    ]
    OUTCOME_CHOICES =[
        ('interested', 'Interested'),
        ('notInterested', 'Not Interested'),
        ('needFollowUp', 'Need Follow Up'),
        ('offerMade', 'Offer Made'),
        ('dealClosed','Deal Closed'),
        ('dealLost', 'Deal Lost')
    ]

    appointment_type = models.CharField(max_length=30, choices=APPOINTMENT_TYPE_CHOICES)
    title = models.TextField()
    sales_case = models.ForeignKey(SalesCase, on_delete=models.CASCADE, related_name='SalesCase')
    scheduled_at = models.DateTimeField()
    scheduled_end = models.DateTimeField()
    location = models.TextField()
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointment_conductor')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointment_creator')
    status = models.CharField(max_length=30, choices=STATUS_CHOICE, default='scheduled')
    outcome = models.CharField(max_length=30, choices=OUTCOME_CHOICES, default='interested')
    notes = models.TextField()
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_created=True)

    def __str__(self):
        return 'Appointment at'+ self.scheduled_at
    
class AppointmentParticipant(models.Model):
    PARTICIPANT_ROLE_CHOICES = [
        ('lead', 'Lead'),
        ('owner', 'Owner'),
        ('partner', 'Partner'),
        ('lawyer', 'Lawyer'),
        ('developer', 'Developer')
    ]
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='Appointment')
    participant = models.ForeignKey(User, null= True, on_delete=models.CASCADE, related_name='Participant')
    participant_name = models.CharField(max_length=150)
    participant_phone = models.CharField(max_length=10)
    participant_email = models.CharField(max_length=150)

    def __str__(self):
        return self.appointment.title + 'attended by' + self.participant_name
