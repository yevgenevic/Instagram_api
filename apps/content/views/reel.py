from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import ModelViewSet

from content.models import Reel
from content.permission import UserPermission
from content.serializers.reel import ReelModelSerializer, UpdateReelModelSerializer


class ReelModelViewSet(ModelViewSet):
    serializer_class = ReelModelSerializer
    queryset = Reel.objects.all()
    parser_classes = (MultiPartParser,)
    permission_classes = (UserPermission,)
    http_method_names = ('get', 'post', 'patch', 'delete')

    def get_serializer_class(self):
        if self.action == 'partial_update':
            return UpdateReelModelSerializer
        return super().get_serializer_class()
