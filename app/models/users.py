from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, max_length=254)
    photo = models.CharField(max_length=255, blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    emergency_contact_name = models.CharField(max_length=255, blank=True, null=True)
    emergency_contact_relationship = models.CharField(max_length=50, blank=True, null=True)
    emergency_contact_phone = models.CharField(max_length=50, blank=True, null=True)
    is_admin = models.BooleanField(default=False)

    # We override these fields from AbstractUser
    first_name = None
    last_name = None
    date_joined = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # Since email is the main identifier now, username becomes secondary

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.email  # or self.username if you'd prefer

