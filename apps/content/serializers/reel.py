from collections import OrderedDict

from rest_framework.fields import SkipField, CharField, HiddenField, CurrentUserDefault
from rest_framework.relations import PKOnlyObject
from rest_framework.serializers import ModelSerializer

from content.models import Reel


class ReelModelSerializer(ModelSerializer):
    id = CharField(read_only=True)
    author = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Reel
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'likes', 'comments', 'id')

    def create(self, validated_data):
        return super().create(validated_data)

    def to_representation(self, instance):
        ret = OrderedDict()
        fields = self._readable_fields

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            check_for_none = attribute.pk if isinstance(attribute, PKOnlyObject) else attribute
            if check_for_none is None:
                ret[field.field_name] = None
            elif hasattr(attribute, 'all'):
                ret[field.field_name] = [field.file.url for field in attribute.all()]
            else:
                ret[field.field_name] = field.to_representation(attribute)
        return ret


class UpdateReelModelSerializer(ModelSerializer):
    class Meta:
        model = Reel
        fields = 'caption', 'location'
        read_only_fields = ('created_at', 'updated_at', 'likes', 'comments', 'id')

    def to_representation(self, instance):
        return ReelModelSerializer(instance).data
