from django.urls import include, path
from rest_framework import routers
from quickstart import views

router = routers.DefaultRouter()
router.get_api_root_view().cls.__name__ = "Test API"
router.get_api_root_view().cls.__doc__ = "Subscribe to NFL teams and players"
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'players', views.PlayerViewSet)
router.register(r'subscriptions', views.SubscriptionViewSet, 'subscriptions')
router.register(r'teams', views.TeamViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
