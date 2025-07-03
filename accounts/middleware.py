from django.utils import timezone
from .models import Session
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import BaseAuthentication

class CustomSessionAuthentication(BaseAuthentication):
    def authenticate(self, request):
        session_token = request.COOKIES.get('sessionId')

        if not session_token:
            return None

        try:
            session = Session.objects.get(session_token=session_token)
            
            if session.expires_at <= timezone.now():
                session.delete()
                raise AuthenticationFailed('Session expired')

            return (session.user, session)

        except Session.DoesNotExist:
            raise AuthenticationFailed('Invalid session token')