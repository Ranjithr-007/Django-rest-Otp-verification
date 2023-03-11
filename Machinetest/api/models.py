from django.db import models

class User(models.Model):
    email_or_phone = models.CharField(max_length=255, unique=True)
    otp = models.CharField(max_length=5)
   


