from rest_framework import viewsets, pagination
from rest_framework.settings import api_settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from . import models as models
from . import serializers as serializers
from .ingestion import ingest_persons


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
    Return a list of all existing Persons
    post:
    Create a new Person
    """
    queryset = models.Person.objects.all().order_by("id")
    serializer_class = serializers.PersonSerializer
    filter_backends = [DjangoFilterBackend]
    # TODO filters
    # filter_class = filters.PersonFilter


class ConditionOccurrenceViewSet(GenericModelViewSet):
    """
    get:
    Return a list of all existing Condition Occurrences
    post:
    Create a new Condition Occurrence
    """
    queryset = models.ConditionOccurrence.objects.all().order_by("id")
    serializer_class = serializers.ConditionOccurrenceSerializer
    filter_backends = [DjangoFilterBackend]
    # TODO filters
    # filter_class = filters.ConditionOccurrenceFilter


class ProcedureOccurrenceViewSet(GenericModelViewSet):
    """
    get:
    Return a list of all existing Procedure Occurrence
    post:
    Create a new Procedure Occurrence
    """
    queryset = models.ProcedureOccurrence.objects.all().order_by("id")
    serializer_class = serializers.ProcedureOccurrenceSerializer
    filter_backends = [DjangoFilterBackend]
    # TODO filters
    # filter_class = filters.ProcedureOccurrenceFilter


class MeasurementViewSet(GenericModelViewSet):
    """
    get:
    Return a list of all existing Measurement
    post:
    Create a new Measurement
    """
    queryset = models.Measurement.objects.all().order_by("id")
    serializer_class = serializers.MeasurementSerializer
    filter_backends = [DjangoFilterBackend]
    # TODO filters
    # filter_class = filters.MeasurementFilter


class ObservationViewSet(GenericModelViewSet):
    """
    get:
    Return a list of all existing Observation
    post:
    Create a new Observation
    """
    queryset = models.Observation.objects.all().order_by("id")
    serializer_class = serializers.ObservationSerializer
    filter_backends = [DjangoFilterBackend]
    # TODO filters
    # filter_class = filters.ObservationFilter


class SpecimenViewSet(GenericModelViewSet):
    """
    get:
    Return a list of all existing Specimen
    post:
    Create a new Specimen
    """
    queryset = models.Specimen.objects.all().order_by("id")
    serializer_class = serializers.SpecimenSerializer
    filter_backends = [DjangoFilterBackend]
    # TODO filters
    # filter_class = filters.SpecimenFilter


@api_view(["POST"])
def ingest(request):
    file = request.data["file"]
    # TODO
    ingest_persons(file)
    return Response(status=204)
