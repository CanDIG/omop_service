from collections import Counter
from rest_framework import viewsets
from rest_framework.settings import api_settings
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination
from . import models as models
from . import serializers as serializers


class LargeResultsSetPagination(pagination.PageNumberPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 10000


class GenericModelViewSet(viewsets.ModelViewSet):
    renderer_classes = (*api_settings.DEFAULT_RENDERER_CLASSES, )
    pagination_class = LargeResultsSetPagination


class PersonViewSet(GenericModelViewSet):
    """
    get:
    Return a list of all existing persons
    post:
    Create a new person
    """
    queryset = models.Person.objects.all().order_by("id")
    serializer_class = serializers.PersonSerializer
    filter_backends = [DjangoFilterBackend]
    # TODO filters
    # filter_class = filters.PersonFilter