from rest_framework import serializers
from .models import SocialMediaAccount

class SocialMediaAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaAccount
        fields = '__all__'