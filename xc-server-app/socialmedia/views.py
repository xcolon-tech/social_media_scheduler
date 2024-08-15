from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import SocialMediaAccount
from .serializers import SocialMediaAccountSerializer

class SocialMediaAccountListCreateView(generics.ListCreateAPIView):
    serializer_class = SocialMediaAccountSerializer

    def get_queryset(self):
        return SocialMediaAccount.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SocialMediaAccountRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SocialMediaAccount.objects.all()
    serializer_class = SocialMediaAccountSerializer

    def get_queryset(self):
        return SocialMediaAccount.objects.filter(user=self.request.user)