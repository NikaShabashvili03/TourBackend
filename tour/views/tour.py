from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from ..models import Tour
from ..serializers.tour import TourSerializer
from accounts.permissions import AllowAny

class TourFeedView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []
    
    def get(self, request):
        search = request.query_params.get('search')
        ordering = request.query_params.get('ordering', '-created_at')
        limit = int(request.query_params.get('limit', 10))
        offset = int(request.query_params.get('offset', 0))

        queryset = Tour.objects.all()

        if search:
            queryset = queryset.filter(
                Q(category__icontains=search)
            )

        if ordering:
            queryset = queryset.order_by(ordering)

        total = queryset.count()
        paginated_queryset = queryset[offset:offset + limit]

        serializer = TourSerializer(paginated_queryset, many=True)
        return Response({
            'results': serializer.data,
            'total': total,
            'limit': limit,
            'offset': offset,
        })


class TourDetailView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def get(self, request, id):
        try:
            tour = Tour.objects.get(id=id)
        except Tour.DoesNotExist:
            return Response({'error': 'Tour not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TourSerializer(tour)
        return Response(serializer.data)