from rest_framework import serializers
from . import models as models


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Person
        fields = '__all__'


class ObservationPeriodSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ObservationPeriod
        fields = '__all__'


class VisitOccurrenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.VisitOccurrence
        fields = '__all__'


class VisitDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.VisitDetail
        fields = '__all__'


class ConditionOccurrenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ConditionOccurrence
        fields = '__all__'


class DrugExposureSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DrugExposure
        fields = '__all__'


class ProcedureOccurrenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProcedureOccurrence
        fields = '__all__'


class DeviceExposureSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DeviceExposure
        fields = '__all__'


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Measurement
        fields = '__all__'


class ObservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Observation
        fields = '__all__'


class NoteNlpSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NoteNlp
        fields = '__all__'


class SpecimenSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Specimen
        fields = '__all__'


class FactRelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FactRelationship
        fields = '__all__'


class SurveyConductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SurveyConduct
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Location
        fields = '__all__'


class LocationHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LocationHistory
        fields = '__all__'


class CareSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CareSite
        fields = '__all__'


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Provider
        fields = '__all__'


class PayerPlanPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PayerPlanPeriod
        fields = '__all__'


class CostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cost
        fields = '__all__'


class DrugEraSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DrugEra
        fields = '__all__'


class DoseEraSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DoseEra
        fields = '__all__'


class ConditionEraSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ConditionEra
        fields = '__all__'


class MetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Metadata
        fields = '__all__'


class CdmSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CdmSource
        fields = '__all__'


class ConceptSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Concept
        fields = '__all__'


class VocabularySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vocabulary
        fields = '__all__'


class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Domain
        fields = '__all__'


class ConceptClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ConceptClass
        fields = '__all__'


class ConceptRelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ConceptRelationship
        fields = '__all__'


class RelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Relationship
        fields = '__all__'


class ConceptSynonymSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ConceptSynonym
        fields = '__all__'


class ConceptAncestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ConceptAncestor
        fields = '__all__'


class SourceToConceptMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SourceToConceptMap
        fields = '__all__'


class DrugStrengthSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DrugStrength
        fields = '__all__'


class CohortSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cohort
        fields = '__all__'


class CohortDefinitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CohortDefinition
        fields = '__all__'
