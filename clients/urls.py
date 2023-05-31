from django.urls import path, include
from rest_framework import routers
from clients.viewsets import ClientsViewSet

router = routers.DefaultRouter()
router.register("clients", ClientsViewSet, basename="clients")


urlpatterns = [
    path("", include(router.urls)),
]
