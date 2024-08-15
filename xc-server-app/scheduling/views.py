from rest_framework import generics
from .models import ScheduledPost
from .serializers import ScheduledPostSerializer

class ScheduledPostListCreateView(generics.ListCreateAPIView):
    serializer_class = ScheduledPostSerializer

    def get_queryset(self):
        return ScheduledPost.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ScheduledPostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ScheduledPost.objects.all()
    serializer_class = ScheduledPostSerializer

    def get_queryset(self):
        return ScheduledPost.objects.filter(user=self.request.user)