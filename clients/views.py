from rest_framework import generics
from clients.models import Case
from clients.serializers import CaseSerializer


class CasesList(generics.ListAPIView):
    """List all Cases"""

    queryset = Case.objects.all()

    serializer_class = CaseSerializer
