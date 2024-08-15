from django.db import models
from django.contrib.auth.models import User

class ScheduledPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    scheduled_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ActivityFeed(models.Model):
    post = models.ForeignKey(ScheduledPost, on_delete=models.CASCADE, related_name='activities')
    activity_description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.activity_description