from django.urls import path
from .views import SocialMediaAccountListCreateView, SocialMediaAccountRetrieveUpdateDestroyView

urlpatterns = [
    path('accounts/', SocialMediaAccountListCreateView.as_view(), name='social-media-account-list-create'),
    path('accounts/<int:pk>/', SocialMediaAccountRetrieveUpdateDestroyView.as_view(), name='social-media-account-detail'),
]