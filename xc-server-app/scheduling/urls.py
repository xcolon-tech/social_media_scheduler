from django.urls import path
from .views import ScheduledPostListCreateView, ScheduledPostRetrieveUpdateDestroyView

urlpatterns = [
    path('posts/', ScheduledPostListCreateView.as_view(), name='scheduled-post-list-create'),
    path('posts/<int:pk>/', ScheduledPostRetrieveUpdateDestroyView.as_view(), name='scheduled-post-detail'),
]