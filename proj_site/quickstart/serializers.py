from django.contrib.auth.models import User, Group
from quickstart.models import Team, Player, Subscription
from rest_framework import serializers


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'city', 'mascot', 'abbreviation', 'wins', 'losses', 'ties']


class PlayerSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)

    class Meta:
        model = Player
        fields = ['id', 'team', 'first_name', 'last_name', 'position', 'yardage', 'touchdowns']


class UserSerializer(serializers.ModelSerializer):
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


class SubscriptionSerializer(serializers.ModelSerializer):
    player = PlayerSerializer(read_only=True)
    team = TeamSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Subscription
        fields = ['id', 'type', 'user', 'player', 'team']

    def validate(self, data):
        """
        A subscription should be for a particular player or team
        """
        if data.get('player') and data.get('team'):
            raise serializers.ValidationError("A subscription can be for a player or a team, not both")
        if data.get('type') == 'Player' and not data.get('player'):
            raise serializers.ValidationError("A Player subscription requires a Player value")
        if data.get('type') == 'Team' and not data.get('team'):
            raise serializers.ValidationError("A Team subscription requires a Team value")
        return data


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'url', 'name']
