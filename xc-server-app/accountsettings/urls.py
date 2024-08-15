from django.urls import path
from .views import UserSettingsRetrieveUpdateView

urlpatterns = [
    path('user-settings/', UserSettingsRetrieveUpdateView.as_view(), name='user-settings'),
]