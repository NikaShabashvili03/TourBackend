from django.urls import path
from ..views.tour import TourFeedView, TourDetailView

urlpatterns = [
    path('feed', TourFeedView.as_view(), name='tour-feed'),
    path('feed/<int:id>', TourDetailView.as_view(), name='tour-details'),
]