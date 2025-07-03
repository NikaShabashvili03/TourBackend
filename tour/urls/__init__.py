from django.urls import path, include

urlpatterns = [
    path('tour/', include('tour.urls.tour')),
    path('order/', include('tour.urls.order'))
]