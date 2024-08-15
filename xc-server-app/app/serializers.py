from rest_framework import serializers
from .models import ScheduledPost, ActivityFeed

class ScheduledPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduledPost
        fields = '__all__'

class ActivityFeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityFeed
        fields = '__all__'