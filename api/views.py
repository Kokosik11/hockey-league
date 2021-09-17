from rest_framework import viewsets
from match.models import Match
from teams.models import Team
from .serializers import MatchSerializer, MatchTeamSerializer, MatchListRetrieveSerializer

class MatchTeamsViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = MatchTeamSerializer


class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

    action_to_serializer = {
        "list": MatchListRetrieveSerializer,
        "retrieve": MatchListRetrieveSerializer,
    }

    def get_serializer_class(self):
        return self.action_to_serializer.get(
            self.action,
            self.serializer_class,
        )
