from django.db import models
from django.contrib.auth.models import User

class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='settings')
    default_language = models.CharField(max_length=10, default='EN')
    
    # App Settings
    calendar_view = models.BooleanField(default=True)
    intelligent_scheduling = models.BooleanField(default=False)
    notification_preferences = models.BooleanField(default=True)
    privacy_security_settings = models.BooleanField(default=True)
    analytics_reporting = models.BooleanField(default=True)

    # Other Settings
    multi_lingual_support = models.BooleanField(default=True)
    security_compliance = models.BooleanField(default=True)

    def __str__(self):
        return f"Settings for {self.user.username}"