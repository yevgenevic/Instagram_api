from django.urls import path, include
from rest_framework.routers import DefaultRouter

from content.models import Reel
from content.views import PostModelViewSet
from content.views.reel import ReelModelViewSet

router = DefaultRouter()
router.register('post', PostModelViewSet, 'posts')
router.register('reel', ReelModelViewSet, 'reels')
urlpatterns = [
    path('', include(router.urls))
]
