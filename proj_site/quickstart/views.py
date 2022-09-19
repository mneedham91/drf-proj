from django.contrib.auth.models import User, Group
from quickstart.models import Team, Player, Subscription
from rest_framework import viewsets
from rest_framework import permissions
from quickstart.serializers import UserSerializer, GroupSerializer, \
     PlayerSerializer, TeamSerializer, SubscriptionSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint for NFL Players
    """
    queryset = Player.objects.all().order_by('-last_name')
    serializer_class = PlayerSerializer
    permission_classes = [permissions.AllowAny]

    # Anyone can GET a player record or list
    # Only Admins can perform other operations
    def get_permissions(self):
        if self.request.method != 'GET':
            return [permissions.IsAdminUser()]
        return super().get_permissions()


class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint for NFL Teams
    """
    queryset = Team.objects.all().order_by('-abbreviation')
    serializer_class = TeamSerializer
    permission_classes = [permissions.AllowAny]

    # Anyone can GET a team record or list
    # Only Admins can perform other operations
    def get_permissions(self):
        if self.request.method != 'GET':
            return [permissions.IsAdminUser()]
        return super().get_permissions()


class SubscriptionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for subscriptions
    """
    queryset = Subscription.objects.all().order_by('-user')
    serializer_class = SubscriptionSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint for users
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint for groups
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
