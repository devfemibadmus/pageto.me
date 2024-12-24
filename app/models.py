from datetime import date
from django.db import models
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.contrib.auth.models import AbstractUser

class templates(models.Model):
    file_name = models.CharField(max_length=50)
    background = models.ImageField(upload_to="templates/background/")

class User(AbstractUser):
    def last_time_default():
        return [0, 0, date.today().strftime("%Y-%m-%d")]
    is_verified = models.BooleanField(default=False)
    minWithdraw = models.IntegerField(default=100)
    documentSubmitted = models.BooleanField(default=False)
    referral = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='referred_users')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password'] 
    
    def __str__(self):
        return f"{self.email}"

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        super().save(*args, **kwargs)

class Pages(models.Model):
    template = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


