from django.db import models
from django.core.validators import EmailValidator

class UserProfile(models.Model):
    email = models.EmailField(max_length=255, unique=True, validators=[EmailValidator()])
    password = models.CharField(max_length=128)  # Store hashed passwords

    def __str__(self):
        return self.email
