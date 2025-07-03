from django.urls import path
from ..views.order import OrderCreateView, OrderFeedView

urlpatterns = [
    path('feed', OrderFeedView.as_view(), name='tour-feed'),
    path('create', OrderCreateView.as_view(), name='tour-details'),
]