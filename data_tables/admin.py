from django.contrib import admin
from . import models as models


# Clinical Data Tables

@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ObservationPeriod)
class ObservationPeriodAdmin(admin.ModelAdmin):
    pass


@admin.register(models.VisitOccurrence)
class VisitOccurrenceAdmin(admin.ModelAdmin):
    pass


@admin.register(models.VisitDetail)
class VisitDetailAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ConditionOccurrence)
class ConditionOccurrenceAdmin(admin.ModelAdmin):
    pass


@admin.register(models.DrugExposure)
class DrugExposureAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ProcedureOccurrence)
class ProcedureOccurrenceAdmin(admin.ModelAdmin):
    pass


@admin.register(models.DeviceExposure)
class DeviceExposureAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Observation)
class ObservationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Note)
class NoteAdmin(admin.ModelAdmin):
    pass


@admin.register(models.NoteNlp)
class NoteNlpAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Specimen)
class SpecimenAdmin(admin.ModelAdmin):
    pass


@admin.register(models.FactRelationship)
class FactRelationshipAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SurveyConduct)
class SurveyConductAdmin(admin.ModelAdmin):
    pass


# Health System Data Tables

@admin.register(models.Location)
class LocationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.LocationHistory)
class LocationHistoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CareSite)
class CareSiteAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Provider)
class ProviderAdmin(admin.ModelAdmin):
    pass


# Health Economic Data Tables

@admin.register(models.PayerPlanPeriod)
class PayerPlanPeriodAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Cost)
class CostAdmin(admin.ModelAdmin):
    pass


# Standardized Derived Elements

@admin.register(models.DrugEra)
class DrugEraAdmin(admin.ModelAdmin):
    pass


@admin.register(models.DoseEra)
class DoseEraAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ConditionEra)
class ConditionEraAdmin(admin.ModelAdmin):
    pass


# Metadata Tables

@admin.register(models.Metadata)
class MetadataAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CdmSource)
class CdmSourceAdmin(admin.ModelAdmin):
    pass


# Vocabulary Tables

@admin.register(models.Concept)
class ConceptAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Vocabulary)
class VocabularyAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Domain)
class DomainAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ConceptClass)
class ConceptClassAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ConceptRelationship)
class ConceptRelationshipAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Relationship)
class RelationshipAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ConceptSynonym)
class ConceptSynonymAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ConceptAncestor)
class ConceptAncestorAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SourceToConceptMap)
class SourceToConceptMapAdmin(admin.ModelAdmin):
    pass


@admin.register(models.DrugStrength)
class DrugStrengthAdmin(admin.ModelAdmin):
    pass


# Cohort

@admin.register(models.Cohort)
class CohortAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CohortDefinition)
class CohortDefinitionAdmin(admin.ModelAdmin):
    pass
