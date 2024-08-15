from django.db import models
from django.contrib.auth.models import User
from socialmedia.models import SocialMediaAccount

class ScheduledPost(models.Model):
    account = models.ForeignKey(SocialMediaAccount, on_delete=models.CASCADE)
    caption = models.CharField(max_length=255)
    content = models.TextField()
    description = models.TextField(blank=True, null=True)
    scheduled_time = models.DateTimeField()

    def __str__(self):
        return f"{self.account.platform} - {self.caption[:20]}"