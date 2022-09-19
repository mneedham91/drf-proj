from django.contrib.auth.models import User, Group
from quickstart.models import Team, Player, Subscription
from rest_framework import serializers


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'city', 'mascot', 'abbreviation', 'wins', 'losses', 'ties']


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'team', 'first_name', 'last_name', 'position', 'yardage', 'touchdowns']


class SubscriptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'type', 'user', 'player', 'team']

    def validate(self, data):
        """
        A subscription should be for a particular player or team
        """
        if data['player'] and data['team']:
            raise serializers.ValidationError("A subscription can be for a player or a team, not both")
        if data['type'] == 'Player' and not data['player']:
            raise serializers.ValidationError("A Player subscription requires a Player value")
        if data['type'] == 'Team' and not data['team']:
            raise serializers.ValidationError("A Team subscription requires a Team value")
        return data


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        return user

    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'password', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'url', 'name']
