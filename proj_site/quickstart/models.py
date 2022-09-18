from django.db import models
from django.conf import settings


class Team(models.Model):
    """
    Data model for NFL team
    """
    city = models.CharField(max_length=15)
    mascot = models.CharField(max_length=15)
    abbreviation = models.CharField(max_length=3)
    wins = models.IntegerField()
    losses = models.IntegerField()
    ties = models.IntegerField()

    def __str__(self):
        return self.abbreviation


class Player(models.Model):
    """
    Data model for NFL player
    """
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    position = models.CharField(max_length=10)
    yardage = models.IntegerField()
    touchdowns = models.IntegerField()

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'


class Subscription(models.Model):
    """
    Data model for a subscription placed by a user on a team or player record
    """
    SUBSCRIPTION_TYPES = (
        ('Team', 'Team'), ('Player', 'Player')
    )
    type = models.CharField(max_length=6, choices=SUBSCRIPTION_TYPES)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE, null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)

    def __str__(self):
        if self.type == 'Team':
            return f'{self.user} - {self.team}'
        elif self.type == 'Player':
            return f'{self.user} - {self.player}'
