from rest_framework import serializers
from match.models import Match
from teams.models import Team


class MatchTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = '__all__'


class MatchSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%d-%m-%Y-%H-%M", input_formats=['%d-%m-%Y-%H-%M'])

    class Meta:
        model = Match
        fields = ('date', 'first_team', 'second_team')


class MatchListRetrieveSerializer(serializers.ModelSerializer):

    first_team = MatchTeamSerializer()
    second_team = MatchTeamSerializer()

    class Meta:
        model = Match
        fields = '__all__'