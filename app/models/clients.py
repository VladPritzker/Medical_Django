from django.db import models

class Client(models.Model):
    email = models.EmailField(unique=True, max_length=254)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    medical_history = models.TextField(blank=True, null=True)
    allergies = models.TextField(blank=True, null=True)
    reason_for_visit = models.CharField(max_length=255, blank=True, null=True)
    appointment_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'clients'

    def __str__(self):
        return self.full_name or self.email
