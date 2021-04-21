from collections import Counter

from rest_framework import viewsets, pagination
from rest_framework.settings import api_settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from . import models as models
from . import serializers as serializers
from .filters import PersonFilter, ConditionOccurrenceFilter
from .ingestion import ingest_generic


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
    filterset_class = PersonFilter


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
    filter_class = ConditionOccurrenceFilter


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
    data_type = request.data["data_type"]
    # TODO add exceptions
    ingest_generic(file, data_type)

    return Response(status=204)


PERSON_PREFETCH = (
    "conditionoccurrence_set",
    "observation_set",
    "measurement_set",
    "specimen_set",
)


@api_view(["GET"])
def overview(request):

    persons = models.Person.objects.all().prefetch_related(*PERSON_PREFETCH)

    persons_gender_counter = Counter()

    conditions_counter = Counter()
    condition_type_counter = Counter()
    observations_counter = Counter()
    measurements_counter = Counter()
    specimens_counter = Counter()

    conditions = set()
    observations = set()
    measurements = set()
    specimens = set()

    for person in persons:

        persons_gender_counter.update((person.gender_concept.concept_name,))

        for c in person.conditionoccurrence_set.all():
            conditions.add(c.id)
            conditions_counter.update((c.condition_concept.concept_name,))
            condition_type_counter.update((c.condition_type_concept.concept_name,))

        for ob in person.observation_set.all():
            observations.add(ob.id)
            observations_counter.update((ob.observation_concept.concept_name,))

        for m in person.measurement_set.all():
            measurements.add(m.id)
            measurements_counter.update((m.measurement_concept.concept_name,))

        for s in person.specimen_set.all():
            specimens.add(s.id)
            specimens_counter.update((s.specimen_concept.concept_name,))

    return Response({
        "persons": {
            "count": persons.count(),
            "gender": dict(persons_gender_counter)
        },
        "conditions": {
            "count": len(conditions),
            "condition": dict(conditions_counter),
            "condition_type": dict(condition_type_counter)
        },
        "observations": {
            "count": len(observations),
            "observation": dict(observations_counter)
        },
        "measurements": {
            "count": len(measurements),
            "measurement": dict(measurements_counter)
        },
        "specimens": {
            "count": len(specimens),
            "specimen": dict(specimens_counter)
        }
    })
