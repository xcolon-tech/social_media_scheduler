from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import ScheduledPost, ActivityFeed
from .serializers import ScheduledPostSerializer, ActivityFeedSerializer

class ScheduledPostListCreateView(generics.ListCreateAPIView):
    queryset = ScheduledPost.objects.all()
    serializer_class = ScheduledPostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ScheduledPostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ScheduledPost.objects.all()
    serializer_class = ScheduledPostSerializer

class ActivityFeedListCreateView(generics.ListCreateAPIView):
    queryset = ActivityFeed.objects.all()
    serializer_class = ActivityFeedSerializer

    def create(self, request, *args, **kwargs):
        post = ScheduledPost.objects.get(id=request.data['post'])
        activity_description = request.data.get('activity_description', '')

        # Creating activity feed
        activity_feed = ActivityFeed.objects.create(post=post, activity_description=activity_description)

        return Response(ActivityFeedSerializer(activity_feed).data, status=status.HTTP_201_CREATED)