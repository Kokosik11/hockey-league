from django.urls import path

from rest_framework import routers
from .views import MatchViewSet, MatchTeamsViewSet

router = routers.SimpleRouter()
router.register('matches', MatchViewSet, basename='matches')
router.register('teams', MatchTeamsViewSet, basename='teams')


urlpatterns = []
urlpatterns += router.urls