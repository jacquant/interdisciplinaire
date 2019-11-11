from rest_framework.serializers import ModelSerializer

from .models import AdaptationAction


class AdaptationActionSerializer(ModelSerializer):
    class Meta:
        model = AdaptationAction
        fields = "__all__"
