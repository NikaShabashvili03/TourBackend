from django.urls import path, include

urlpatterns = [
    path('user/', include('accounts.urls.user')),
]