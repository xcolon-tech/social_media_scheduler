from django.urls import path
from .views import ScheduledPostListCreateView, ScheduledPostRetrieveUpdateDestroyView, ActivityFeedListCreateView

urlpatterns = [
    path('posts/', ScheduledPostListCreateView.as_view(), name='scheduled-post-list-create'),
    path('posts/<int:pk>/', ScheduledPostRetrieveUpdateDestroyView.as_view(), name='scheduled-post-detail'),
    path('activities/', ActivityFeedListCreateView.as_view(), name='activity-feed-list-create'),
]