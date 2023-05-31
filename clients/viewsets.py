from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from clients.serializers import ClientSerializer
from clients.models import Client


class ClientsViewSet(viewsets.ModelViewSet):
    """Display Clients"""

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["name"]
    search_fields = ["name", "document"]
    filterset_fields = ["is_active"]
