from django.urls import path, include
from rest_framework import routers
from clients.viewsets import ClientsViewSet
from clients.views import CasesList

router = routers.DefaultRouter()
router.register("clients", ClientsViewSet, basename="clients")


urlpatterns = [
    path("", include(router.urls)),
    path("cases/", CasesList.as_view()),
]
