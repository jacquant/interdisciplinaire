from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView
from rest_framework import viewsets

from .models import AdaptationAction
from .serializers import AdaptationActionSerializer

index_view = never_cache(TemplateView.as_view(template_name="index.html"))


class AdaptationActionView(viewsets.ModelViewSet):
    serializer_class = AdaptationActionSerializer
    queryset = AdaptationAction.objects.all()
