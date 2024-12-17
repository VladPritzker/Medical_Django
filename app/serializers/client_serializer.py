from rest_framework import serializers
from app.models.clients import Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            'id',
            'email',
            'full_name',
            'phone_number',
            'medical_history',
            'allergies',
            'reason_for_visit',
            'appointment_date',
        ]
