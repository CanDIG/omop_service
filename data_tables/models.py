# The docs strings (c) https://github.com/OHDSI/CommonDataModel/blob/master/LICENSE
# The OMOP documentation: https://ohdsi.github.io/CommonDataModel/index.html

from django.db import models


# TODO check this it's not in the docs but in SQL statement
# class AttributeDefinition(models.Model):
#     attribute_definition_id = models.IntegerField()
#     attribute_name = models.CharField(max_length=255)
#     attribute_description = models.TextField(blank=True, null=True)
#     attribute_type_concept_id = models.IntegerField()
#     attribute_syntax = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'attribute_definition'


# related name is class name + '_' + field name


# Clinical Data Tables


class Person(models.Model):
    """
    The Person Domain contains records that uniquely identify each patient in the source data
    who is time at-risk to have clinical observations recorded within the source systems.
    """
    person_id = models.CharField(unique=True, max_length=200)
    gender_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                       related_name='person_gender_concept')
    year_of_birth = models.IntegerField(blank=True, null=True)
    month_of_birth = models.IntegerField(blank=True, null=True)
    day_of_birth = models.IntegerField(blank=True, null=True)
    birth_datetime = models.DateTimeField(blank=True, null=True)
    death_datetime = models.DateTimeField(blank=True, null=True)
    race_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                     related_name='person_race_concept')
    ethnicity_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                          related_name='person_ethnicity_concept')
    location = models.ForeignKey("Location", on_delete=models.SET_NULL, blank=True, null=True)
    provider = models.ForeignKey("Provider", on_delete=models.SET_NULL, blank=True, null=True)
    care_site = models.ForeignKey("CareSite", on_delete=models.SET_NULL, blank=True, null=True)
    person_source_value = models.CharField(max_length=200, blank=True)
    gender_source_value = models.CharField(max_length=200, blank=True)
    gender_source_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                              related_name='person_gender_source_concept')
    race_source_value = models.CharField(max_length=200, blank=True)
    race_source_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                            related_name='person_race_source_concept')
    ethnicity_source_value = models.CharField(max_length=200, blank=True)
    ethnicity_source_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                                 related_name='person_ethnicity_source_concept')

    def __str__(self):
        return str(self.person_id)


class ObservationPeriod(models.Model):
    """
    The OBSERVATION_PERIOD table contains records which uniquely define the spans of time
    for which a Person is at-risk to have clinical events recorded within the source systems,
    even if no events in fact are recorded (healthy patient with no healthcare interactions).
    """
    observation_period_id = models.CharField(unique=True, max_length=200)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    observation_period_start_date = models.DateField(blank=True, null=True)
    observation_period_end_date = models.DateField(blank=True, null=True)
    period_type_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.observation_period_id)


class VisitOccurrence(models.Model):
    """
    Contains the spans of time a Person continuously receives medical services
    from one or more providers at a Care Site in a given setting within the health care system.
    """
    visit_occurrence_id = models.CharField(unique=True, max_length=200)
    person = models.ForeignKey(Person, models.CASCADE)
    visit_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                      related_name='visit_occurrence_visit_concept')
    visit_start_date = models.DateField(blank=True, null=True)
    visit_start_datetime = models.DateTimeField(blank=True, null=True)
    visit_end_date = models.DateField(blank=True, null=True)
    visit_end_datetime = models.DateTimeField(blank=True, null=True)
    visit_type_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                           related_name='visit_occurrence_visit_type_concept')
    provider = models.ForeignKey('Provider', on_delete=models.SET_NULL, blank=True, null=True)
    care_site = models.ForeignKey('CareSite', on_delete=models.SET_NULL, blank=True, null=True)
    visit_source_value = models.CharField(max_length=200, blank=True)
    visit_source_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                             related_name='visit_occurrence_visit_source_concept')
    admitted_from_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                              related_name='visit_occurrence_admitted_from_concept')
    admitted_from_source_value = models.CharField(max_length=200, blank=True)
    discharge_to_source_value = models.CharField(max_length=200, blank=True)
    discharge_to_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                             related_name='visit_occurrence_discharge_to_concept')
    preceding_visit_occurrence = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.visit_occurrence_id)


class VisitDetail(models.Model):
    """
    The VISIT_DETAIL table is an optional table used to represents details
    of each record in the parent visit_occurrence table.
    """
    visit_detail_id = models.CharField(unique=True, max_length=200)
    person = models.ForeignKey(Person, models.CASCADE)
    visit_detail_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                             related_name='visit_detail_visit_detail_concept')
    visit_detail_start_date = models.DateField(blank=True, null=True)
    visit_detail_start_datetime = models.DateTimeField(blank=True, null=True)
    visit_detail_end_date = models.DateField(blank=True, null=True)
    visit_detail_end_datetime = models.DateTimeField(blank=True, null=True)
    visit_detail_type_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                                  related_name='visit_detail_visit_detail_type_concept')
    provider = models.ForeignKey('Provider', on_delete=models.SET_NULL, blank=True, null=True)
    care_site = models.ForeignKey('CareSite', on_delete=models.SET_NULL, blank=True, null=True)
    discharge_to_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                             related_name='visit_detail_discharge_to_concept')
    admitted_from_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                              related_name='visit_detail_admitted_from_concept')
    admitted_from_source_value = models.CharField(max_length=200, blank=True)
    visit_detail_source_value = models.CharField(max_length=200, blank=True)
    visit_detail_source_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                                    related_name='visit_detail_visit_detail_source_concept')
    discharge_to_source_value = models.CharField(max_length=200, blank=True)
    preceding_visit_detail = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True,
                                               related_name='visit_detail_visit_detail_preceding_visit_detail')
    visit_detail_parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True,
                                            related_name='visit_detail_visit_detail_visit_detail_parent')
    visit_occurrence = models.ForeignKey('VisitOccurrence', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.visit_detail_id)


class ConditionOccurrence(models.Model):
    """
    Conditions are records of a Person suggesting the presence of a disease
    or medical condition stated as a diagnosis, a sign, or a symptom,
    which is either observed by a Provider or reported by the patient.
    """
    condition_occurrence_id = models.CharField(unique=True, max_length=200)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    condition_concept = models.ForeignKey('Concept', models.SET_NULL, blank=True, null=True,
                                          related_name='condition_occurrence_condition_concept')
    condition_start_date = models.DateField(blank=True, null=True)
    condition_start_datetime = models.DateTimeField(blank=True, null=True)
    condition_end_date = models.DateField(blank=True, null=True)
    condition_end_datetime = models.DateTimeField(blank=True, null=True)
    condition_type_concept = models.ForeignKey('Concept', models.SET_NULL, blank=True, null=True,
                                               related_name='condition_occurrence_condition_type_concept')
    condition_status_concept = models.ForeignKey('Concept', models.SET_NULL, blank=True, null=True,
                                                 related_name='condition_occurrence_condition_status_concept')
    stop_reason = models.CharField(max_length=20, blank=True)
    provider = models.ForeignKey('Provider', models.SET_NULL, blank=True, null=True)
    visit_occurrence = models.ForeignKey('VisitOccurrence', models.SET_NULL, blank=True, null=True,
                                         related_name='condition_occurrence_visit_occurrence')
    visit_detail = models.ForeignKey('VisitDetail', models.SET_NULL, blank=True, null=True,
                                     related_name='condition_occurrence_visit_detail')
    condition_source_value = models.CharField(max_length=50, blank=True)
    condition_source_concept = models.ForeignKey('Concept', models.SET_NULL, blank=True, null=True,
                                                 related_name='condition_occurrence_condition_source_concept')
    condition_status_source_value = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return str(self.condition_occurrence_id)


class DrugExposure(models.Model):
    """
    Drug Exposure is inferred from clinical events associated with orders,
    prescriptions written, pharmacy dispensings, procedural administrations,
    and other patient-reported information.
    """
    drug_exposure_id = models.CharField(unique=True, max_length=200)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    drug_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                     related_name='drug_exposure_drug_concept')
    drug_exposure_start_date = models.DateField(blank=True, null=True)
    drug_exposure_start_datetime = models.DateTimeField(blank=True, null=True)
    drug_exposure_end_date = models.DateField(blank=True, null=True)
    drug_exposure_end_datetime = models.DateTimeField(blank=True, null=True)
    verbatim_end_date = models.DateField(blank=True, null=True)
    drug_type_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                          related_name='drug_exposure_drug_type_concept')
    stop_reason = models.CharField(max_length=200, blank=True)
    refills = models.IntegerField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    days_supply = models.IntegerField(blank=True, null=True)
    sig = models.TextField(blank=True, null=True)
    route_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                      related_name='drug_exposure_route_concept')
    lot_number = models.CharField(max_length=200, blank=True)
    provider = models.ForeignKey('Provider', on_delete=models.SET_NULL, blank=True, null=True)
    visit_occurrence = models.ForeignKey('VisitOccurrence', on_delete=models.SET_NULL, blank=True, null=True)
    visit_detail = models.ForeignKey('VisitDetail', on_delete=models.SET_NULL, blank=True, null=True)
    drug_source_value = models.CharField(max_length=200, blank=True)
    drug_source_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                            related_name='drug_exposure_drug_source_concept')
    route_source_value = models.CharField(max_length=200, blank=True)
    dose_unit_source_value = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return str(self.drug_exposure_id)


class ProcedureOccurrence(models.Model):
    """
    The PROCEDURE_OCCURRENCE table contains records of activities
    or processes ordered by, or carried out by, a healthcare provider
    on the patient to have a diagnostic or therapeutic purpose.
    """
    procedure_occurrence_id = models.CharField(unique=True, max_length=200)
    person = models.ForeignKey(Person, models.CASCADE)
    procedure_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                          related_name='procedure_occurrence_procedure_concept')
    procedure_date = models.DateField(blank=True, null=True)
    procedure_datetime = models.DateTimeField(blank=True, null=True)
    procedure_type_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                               related_name='procedure_occurrence_procedure_type_concept')
    modifier_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                         related_name='procedure_occurrence_modifier_concept')
    quantity = models.IntegerField(blank=True, null=True)
    provider = models.ForeignKey('Provider', models.SET_NULL, blank=True, null=True)
    visit_occurrence = models.ForeignKey('VisitOccurrence', models.SET_NULL, blank=True, null=True)
    visit_detail = models.ForeignKey('VisitDetail', models.SET_NULL, blank=True, null=True)
    procedure_source_value = models.CharField(max_length=200, blank=True)
    procedure_source_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                                 related_name='procedure_occurrence_procedure_source_concept')
    modifier_source_value = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return str(self.procedure_occurrence_id)


class DeviceExposure(models.Model):
    """
    The 'Device' domain captures information about a person's exposure
    to a foreign physical object or instrument which is used for diagnostic
    or therapeutic purposes through a mechanism beyond chemical action.
    """
    device_exposure_id = models.CharField(unique=True, max_length=200)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    device_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                       related_name='device_exposure_device_concept')
    device_exposure_start_date = models.DateField(blank=True, null=True)
    device_exposure_start_datetime = models.DateTimeField(blank=True, null=True)
    device_exposure_end_date = models.DateField(blank=True, null=True)
    device_exposure_end_datetime = models.DateTimeField(blank=True, null=True)
    device_type_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                            related_name='device_exposure_device_type_concept')
    unique_device_id = models.CharField(max_length=200, blank=True)
    quantity = models.IntegerField(blank=True, null=True)
    provider = models.ForeignKey('Provider', on_delete=models.SET_NULL, blank=True, null=True)
    visit_occurrence = models.ForeignKey('VisitOccurrence', on_delete=models.SET_NULL, blank=True, null=True)
    visit_detail = models.ForeignKey('VisitDetail', on_delete=models.SET_NULL, blank=True, null=True)
    device_source_value = models.CharField(max_length=200, blank=True)
    device_source_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                              related_name='device_exposure_device_source_concept')

    def __str__(self):
        return str(self.device_exposure_id)


class Measurement(models.Model):
    """
    The MEASUREMENT table contains both orders and results of such Measurements
    as laboratory tests, vital signs, quantitative findings from pathology reports, etc.
    """
    measurement_id = models.CharField(unique=True, max_length=200)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    measurement_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                            related_name='measurement_measurement_concept')
    measurement_date = models.DateField(blank=True, null=True)
    measurement_datetime = models.DateTimeField(blank=True, null=True)
    measurement_type_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                                 related_name='measurement_measurement_type_concept')
    operator_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                         related_name='measurement_operator_concept')
    value_as_number = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    value_as_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                         related_name='measurement_value_as_concept')
    unit_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                     related_name='measurement_unit_concept')
    range_low = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    range_high = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    provider = models.ForeignKey('Provider', on_delete=models.SET_NULL, blank=True, null=True)
    visit_occurrence = models.ForeignKey('VisitOccurrence', on_delete=models.SET_NULL, blank=True, null=True)
    visit_detail = models.ForeignKey('VisitDetail', on_delete=models.SET_NULL, blank=True, null=True)
    measurement_source_value = models.CharField(max_length=200, blank=True)
    measurement_source_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                                   related_name='measurement_measurement_source_concept')
    unit_source_value = models.CharField(max_length=200, blank=True)
    value_source_value = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return str(self.measurement_id)


class Observation(models.Model):
    """
    The OBSERVATION table captures clinical facts about a Person
    obtained in the context of examination, questioning or a procedure.
    """
    observation_id = models.CharField(unique=True, max_length=200)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    observation_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                            related_name='observation_observation_concept')
    observation_date = models.DateField(blank=True, null=True)
    observation_datetime = models.DateTimeField(blank=True, null=True)
    observation_type_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                                 related_name='observation_observation_type_concept')
    value_as_number = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    value_as_string = models.CharField(max_length=200, blank=True)
    value_as_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                         related_name='observation_value_as_concept')
    qualifier_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                          related_name='observation_qualifier_concept')
    unit_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                     related_name='observation_unit_concept')
    provider = models.ForeignKey('Provider', on_delete=models.SET_NULL, blank=True, null=True)
    visit_occurrence = models.ForeignKey('VisitOccurrence', on_delete=models.SET_NULL, blank=True, null=True)
    visit_detail = models.ForeignKey('VisitDetail', on_delete=models.SET_NULL, blank=True, null=True)
    observation_source_value = models.CharField(max_length=200, blank=True)
    observation_source_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                                   related_name='observation_observation_source_concept')
    unit_source_value = models.CharField(max_length=200, blank=True)
    qualifier_source_value = models.CharField(max_length=200, blank=True)
    observation_event = models.ForeignKey("ProcedureOccurrence", on_delete=models.SET_NULL, blank=True, null=True)
    obs_event_field_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                                related_name='observation_obs_event_field_concept')
    value_as_datetime = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.observation_id)


class Note(models.Model):
    """
    The NOTE table captures unstructured information that was recorded
    by a provider about a patient in free text notes on a given date.
    """
    note_id = models.CharField(unique=True, max_length=200)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    note_date = models.DateField(blank=True, null=True)
    note_datetime = models.DateTimeField(blank=True, null=True)
    note_type_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                          related_name='note_note_type_concept')
    note_class_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                           related_name='note_note_class_concept')
    note_title = models.CharField(max_length=250, blank=True)
    note_text = models.TextField(blank=True)
    encoding_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                         related_name='note_encoding_concept')
    language_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                         related_name='note_language_concept')
    provider = models.ForeignKey('Provider', on_delete=models.SET_NULL, blank=True, null=True)
    visit_occurrence = models.ForeignKey('VisitOccurrence', on_delete=models.SET_NULL, blank=True, null=True)
    visit_detail = models.ForeignKey('VisitDetail', on_delete=models.SET_NULL, blank=True, null=True)
    note_source_value = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return str(self.note_id)


class NoteNlp(models.Model):
    """
    The NOTE_NLP table will encode all output of NLP on clinical notes.
    Each row represents a single extracted term from a note.
    """
    note_nlp_id = models.CharField(unique=True, max_length=200)
    note = models.ForeignKey(Note, models.CASCADE)
    section_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                        related_name='note_nlp_section_concept')
    snippet = models.CharField(max_length=250, blank=True)
    offset = models.CharField(max_length=250, blank=True)
    lexical_variant = models.CharField(max_length=250)
    note_nlp_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                         related_name='note_nlp_note_nlp_concept')
    nlp_system = models.CharField(max_length=250, blank=True)
    nlp_date = models.DateField(blank=True, null=True)
    nlp_datetime = models.DateTimeField(blank=True, null=True)
    # TODO check this field type
    term_exists = models.CharField(max_length=1, blank=True)
    term_temporal = models.CharField(max_length=200, blank=True)
    term_modifiers = models.CharField(max_length=2000, blank=True)
    note_nlp_source_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                                related_name='note_nlp_note_nlp_source_concept')

    def __str__(self):
        return str(self.note_nlp_id)


class Specimen(models.Model):
    """
    The specimen domain contains the records identifying biological samples from a person.
    """
    specimen_id = models.CharField(unique=True, max_length=200)
    person = models.ForeignKey(Person, models.CASCADE)
    specimen_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                         related_name='specimen_specimen_concept')
    specimen_type_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                              related_name='specimen_specimen_type_concept')
    specimen_date = models.DateField(blank=True, null=True)
    specimen_datetime = models.DateTimeField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    unit_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                     related_name='specimen_unit_concept')
    anatomic_site_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                              related_name='specimen_anatomic_site_concept')
    disease_status_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                               related_name='specimen_disease_status_concept')
    specimen_source_id = models.CharField(max_length=200, blank=True)
    specimen_source_value = models.CharField(max_length=200, blank=True)
    unit_source_value = models.CharField(max_length=200, blank=True)
    anatomic_site_source_value = models.CharField(max_length=200, blank=True)
    disease_status_source_value = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return str(self.specimen_id)


class FactRelationship(models.Model):
    """
    The FACT_RELATIONSHIP table contains records about
    the relationships between facts stored as records in any table of the CDM.
    """
    domain_concept_id_1 = models.ForeignKey('Concept', models.CASCADE, db_column='domain_concept_id_1',
                                            related_name='fact_relationship_domain_concept_id_1')
    fact_id_1 = models.BigIntegerField(null=True)
    domain_concept_id_2 = models.ForeignKey('Concept', models.CASCADE, db_column='domain_concept_id_2',
                                            related_name='fact_relationship_domain_concept_id_2')
    fact_id_2 = models.BigIntegerField(null=True)
    relationship_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                             related_name='fact_relationship_relationship_concept')

    def __str__(self):
        return str(self.id)


class SurveyConduct(models.Model):
    """
    The SURVEY_CONDUCT table is used to store an instance of a completed survey or questionnaire.
    """
    survey_conduct_id = models.CharField(unique=True, max_length=200)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    survey_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                       related_name='survey_conduct_survey_concept')
    survey_start_date = models.DateField(blank=True, null=True)
    survey_start_datetime = models.DateTimeField(blank=True, null=True)
    survey_end_date = models.DateField(blank=True, null=True)
    survey_end_datetime = models.DateTimeField(blank=True, null=True)
    provider = models.ForeignKey('Provider', on_delete=models.SET_NULL, blank=True, null=True)
    assisted_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                         related_name='survey_conduct_assisted_concept')
    respondent_type_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                                related_name='survey_conduct_respondent_type_concept')
    timing_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                       related_name='survey_conduct_timing_concept')
    collection_method_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                                  related_name='survey_conduct_collection_method_concept')
    assisted_source_value = models.CharField(max_length=200, blank=True)
    respondent_type_source_value = models.CharField(max_length=200, blank=True)
    timing_source_value = models.CharField(max_length=200, blank=True)
    collection_method_source_value = models.CharField(max_length=200, blank=True)
    survey_source_value = models.CharField(max_length=200, blank=True)
    survey_source_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                              related_name='survey_conduct_survey_source_concept')
    survey_source_identifier = models.CharField(max_length=200, blank=True)
    validated_survey_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                                 related_name='survey_conduct_validated_survey_concept')
    validated_survey_source_value = models.CharField(max_length=200, blank=True)
    survey_version_number = models.CharField(max_length=200, blank=True)
    visit_occurrence = models.ForeignKey('VisitOccurrence', on_delete=models.SET_NULL, blank=True, null=True,
                                         related_name='survey_conduct_visit_occurrence')
    visit_detail = models.ForeignKey('VisitDetail', on_delete=models.SET_NULL, blank=True, null=True)
    response_visit_occurrence = models.ForeignKey('VisitOccurrence', on_delete=models.SET_NULL, blank=True, null=True,
                                                  related_name='survey_conduct_response_visit_occurrence')

    def __str__(self):
        return str(self.survey_conduct_id)


# Health System Data Tables


class Location(models.Model):
    """
    The LOCATION table represents a generic way to capture physical location
    or address information of Persons and Care Sites.
    """
    location_id = models.CharField(unique=True, max_length=200)
    address_1 = models.CharField(max_length=200, blank=True)
    address_2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    zip = models.CharField(max_length=50, blank=True, null=True)
    county = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    location_source_value = models.CharField(max_length=200, blank=True)
    latitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    longitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    def __str__(self):
        return str(self.location_id)


class LocationHistory(models.Model):
    """
    The LOCATION HISTORY table stores relationships between Persons
    or Care Sites and geographic locations over time.
    """
    location_history_id = models.CharField(unique=True, max_length=200)
    location = models.ForeignKey(Location, models.CASCADE)
    relationship_type_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True)
    domain_id = models.CharField(max_length=200, blank=True)
    # TODO References either person_id, provider_id, or care_site_id, depending on domain_id.
    entity_id = models.BigIntegerField(null=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.location_history_id)


class CareSite(models.Model):
    """
    The CARE_SITE table contains a list of uniquely identified institutional (physical or organizational) units
    where healthcare delivery is practiced (offices, wards, hospitals, clinics, etc.).
    """
    care_site_id = models.CharField(unique=True, max_length=200)
    care_site_name = models.CharField(max_length=500, blank=True, null=True)
    place_of_service_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True)
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, blank=True, null=True)
    care_site_source_value = models.CharField(max_length=200, blank=True)
    place_of_service_source_value = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return str(self.care_site_id)


class Provider(models.Model):
    """
    The PROVIDER table contains a list of uniquely identified healthcare providers.
    """
    provider_id = models.CharField(unique=True, max_length=200)
    provider_name = models.CharField(max_length=500, blank=True, null=True)
    npi = models.CharField(max_length=200, blank=True)
    dea = models.CharField(max_length=200, blank=True)
    specialty_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                          related_name='provider_specialty_concept')
    care_site = models.ForeignKey(CareSite, on_delete=models.SET_NULL, blank=True, null=True)
    year_of_birth = models.IntegerField(blank=True, null=True)
    gender_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                       related_name='provider_gender_concept')
    provider_source_value = models.CharField(max_length=200, blank=True)
    specialty_source_value = models.CharField(max_length=200, blank=True)
    specialty_source_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                                 related_name='provider_specialty_source_concept')
    gender_source_value = models.CharField(max_length=200, blank=True)
    gender_source_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                              related_name='provider_gender_source_concept')

    def __str__(self):
        return str(self.provider_id)


# Health Economic Data Tables


class PayerPlanPeriod(models.Model):
    """
    The PAYER_PLAN_PERIOD table captures details of the period of time that
    a Person is continuously enrolled under a specific health Plan benefit structure from a given Payer.
    """
    payer_plan_period_id = models.CharField(unique=True, max_length=200)
    person = models.ForeignKey('Person', on_delete=models.CASCADE,
                               related_name='payer_plan_period_person')
    contract_person = models.ForeignKey('Person', on_delete=models.SET_NULL, blank=True, null=True,
                                        related_name='payer_plan_period_contract_person')
    payer_plan_period_start_date = models.DateField(blank=True, null=True)
    payer_plan_period_end_date = models.DateField(blank=True, null=True)
    payer_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                      related_name='payer_plan_period_payer_concept')
    plan_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                     related_name='payer_plan_period_plan_concept')
    contract_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                         related_name='payer_plan_period_contract_concept')
    sponsor_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                        related_name='payer_plan_period_sponsor_concept')
    stop_reason_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                            related_name='payer_plan_period_stop_reason_concept')
    payer_source_value = models.CharField(max_length=200, blank=True)
    payer_source_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                             related_name='payer_plan_period_payer_source_concept')
    plan_source_value = models.CharField(max_length=200, blank=True)
    plan_source_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                            related_name='payer_plan_period_plan_source_concept')
    contract_source_value = models.CharField(max_length=200, blank=True)
    contract_source_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                                related_name='payer_plan_period_contract_source_concept')
    sponsor_source_value = models.CharField(max_length=200, blank=True)
    sponsor_source_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                               related_name='payer_plan_period_sponsor_source_concept')
    family_source_value = models.CharField(max_length=200, blank=True)
    stop_reason_source_value = models.CharField(max_length=200, blank=True)
    stop_reason_source_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                                   related_name='payer_plan_period_stop_reason_source_concept')

    def __str__(self):
        return str(self.payer_plan_period_id)


class Cost(models.Model):
    """
    The COST table captures records containing the cost of any medical event
    recorded in one of the OMOP clinical event tables
    """
    cost_id = models.CharField(unique=True, max_length=200)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    cost_event_id = models.BigIntegerField(null=True)
    cost_event_field_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                                 related_name='cost_cost_event_field_concept')
    cost_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                     related_name='cost_cost_concept')
    cost_type_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                          related_name='cost_cost_type_concept')
    currency_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                         related_name='cost_currency_concept')
    cost = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    incurred_date = models.DateField(blank=True, null=True)
    billed_date = models.DateField(blank=True, null=True)
    paid_date = models.DateField(blank=True, null=True)
    revenue_code_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                             related_name='cost_revenue_code_concept')
    drg_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                    related_name='cost_drg_concept')
    cost_source_value = models.CharField(max_length=200, blank=True)
    cost_source_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                            related_name='cost_cost_source_concept')
    revenue_code_source_value = models.CharField(max_length=200, blank=True)
    drg_source_value = models.CharField(max_length=200, blank=True, null=True)
    payer_plan_period = models.ForeignKey('PayerPlanPeriod', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.cost_id)


# Standardized Derived Elements


class DrugEra(models.Model):
    """
    A Drug Era is defined as a span of time when the Person is assumed
    to be exposed to a particular active ingredient.
    """
    drug_era_id = models.CharField(unique=True, max_length=200)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    drug_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True)
    drug_era_start_datetime = models.DateTimeField(blank=True, null=True)
    drug_era_end_datetime = models.DateTimeField(blank=True, null=True)
    drug_exposure_count = models.IntegerField(blank=True, null=True)
    gap_days = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.drug_era_id)


class DoseEra(models.Model):
    """
    A Dose Era is defined as a span of time when the Person is assumed to be exposed
    to a constant dose of a specific active ingredient.
    """
    dose_era_id = models.CharField(unique=True, max_length=200)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    drug_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                     related_name='dose_era_drug_concept')
    unit_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                     related_name='dose_era_unit_concept')
    dose_value = models.DecimalField(max_digits=65535, decimal_places=65535)
    dose_era_start_datetime = models.DateTimeField(blank=True, null=True)
    dose_era_end_datetime = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.dose_era_id)


class ConditionEra(models.Model):
    """
    A Condition Era is defined as a span of time when the Person is assumed to have a given condition.
    """
    condition_era_id = models.CharField(unique=True, max_length=200)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    condition_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True)
    condition_era_start_datetime = models.DateTimeField(blank=True, null=True)
    condition_era_end_datetime = models.DateTimeField(blank=True, null=True)
    condition_occurrence_count = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.condition_era_id)


# Metadata Tables


class Metadata(models.Model):
    """
    The METADATA table contains metadata information about a dataset that
    has been transformed to the OMOP Common Data Model.
    """
    metadata_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                         related_name='metadata_metadata_concept')
    metadata_type_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                              related_name='metadata_metadata_type_concept')
    name = models.CharField(max_length=255, blank=True)
    value_as_string = models.TextField(blank=True)
    value_as_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                         related_name='metadata_value_as_concept')
    metadata_date = models.DateField(blank=True, null=True)
    metadata_datetime = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class CdmSource(models.Model):
    """
    The CDM_SOURCE table contains detail about the source database and the process
    used to transform the data into the OMOP Common Data Model.
    """
    cdm_source_name = models.CharField(max_length=255)
    cdm_source_abbreviation = models.CharField(max_length=200, blank=True)
    cdm_holder = models.CharField(max_length=500, blank=True)
    source_description = models.TextField(blank=True)
    source_documentation_reference = models.CharField(max_length=255, blank=True)
    cdm_etl_reference = models.CharField(max_length=255, blank=True)
    source_release_date = models.DateField(blank=True, null=True)
    cdm_release_date = models.DateField(blank=True, null=True)
    cdm_version = models.CharField(max_length=200, blank=True)
    vocabulary_version = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return str(self.id)


# Vocabulary Tables


class Concept(models.Model):
    """
    Concepts uniquely identify each fundamental unit of meaning
    used to express clinical information in all domain tables of the CDM.
    """
    # form the source SQL
    # concept_id = models.IntegerField(primary_key=True)
    concept_id = models.CharField(unique=True, max_length=200)
    concept_name = models.CharField(max_length=255, blank=True)
    domain = models.ForeignKey('Domain', on_delete=models.SET_NULL, null=True, blank=True)
    vocabulary = models.ForeignKey('Vocabulary', on_delete=models.SET_NULL, null=True, blank=True)
    concept_class = models.ForeignKey('ConceptClass', on_delete=models.SET_NULL, null=True, blank=True)
    # S - standard concept, C - Classification concept
    standard_concept = models.CharField(max_length=2, choices=[("S", "S"), ("C", "C")], blank=True, null=True)
    concept_code = models.CharField(max_length=200, blank=True)
    valid_start_date = models.DateField(null=True, blank=True)
    valid_end_date = models.DateField(null=True, blank=True)
    # D - deleted, U - updated
    invalid_reason = models.CharField(max_length=2, choices=[("D", "D"), ("U", "U")], blank=True, null=True)

    def __str__(self):
        return str(self.concept_id)


class Vocabulary(models.Model):
    """
    The VOCABULARY table includes a list of the Vocabularies
    collected from various sources or created de novo by the OMOP community.
    """
    vocabulary_id = models.CharField(unique=True, max_length=200)
    vocabulary_name = models.CharField(max_length=255, blank=True)
    vocabulary_reference = models.CharField(max_length=255, blank=True)
    vocabulary_version = models.CharField(max_length=255, blank=True, null=True)
    vocabulary_concept = models.ForeignKey(Concept, on_delete=models.SET_NULL, null=True, blank=True,
                                           related_name='vocabulary_vocabulary_concept')

    def __str__(self):
        return str(self.vocabulary_id)


class Domain(models.Model):
    """
    The DOMAIN table includes a list of OMOP-defined Domains
    the Concepts of the Standardized Vocabularies can belong to.
    """

    domain_id = models.CharField(unique=True, max_length=200)
    domain_name = models.CharField(max_length=255, blank=True)
    domain_concept = models.ForeignKey(Concept, on_delete=models.SET_NULL, null=True, blank=True,
                                       related_name='domain_domain_concept')

    def __str__(self):
        return str(self.domain_id)


class ConceptClass(models.Model):
    """
    The CONCEPT_CLASS table is a reference table, which includes a list of the classifications
    used to differentiate Concepts within a given Vocabulary.
    """
    concept_class_id = models.CharField(unique=True, max_length=200)
    concept_class_name = models.CharField(max_length=255, blank=True)
    concept_class_concept = models.ForeignKey(Concept, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.concept_class_id)


class ConceptRelationship(models.Model):
    """
    The CONCEPT_RELATIONSHIP table contains records that define direct relationships
    between any two Concepts and the nature or type of the relationship.
    """
    concept_id_1 = models.OneToOneField(Concept, on_delete=models.CASCADE,
                                        related_name='concept_relationship_concept_id_1')
    concept_id_2 = models.ForeignKey(Concept, on_delete=models.SET_NULL, null=True, blank=True,
                                     related_name='concept_relationship_concept_id_2')
    relationship = models.ForeignKey('Relationship', on_delete=models.SET_NULL, null=True, blank=True)
    valid_start_date = models.DateField(null=True, blank=True)
    valid_end_date = models.DateField(null=True, blank=True)
    # D - deleted, U - updated
    invalid_reason = models.CharField(max_length=2, choices=[("D", "D"), ("U", "U")], blank=True, null=True)

    def __str__(self):
        return str(self.concept_id_1)


class Relationship(models.Model):
    """
    The RELATIONSHIP table provides a reference list of all types of relationships
    that can be used to associate any two concepts in the CONCEPT_RELATIONSHP table.
    """
    relationship_id = models.CharField(unique=True, max_length=200)
    relationship_name = models.CharField(max_length=255, blank=True)
    is_hierarchical = models.BooleanField()
    defines_ancestry = models.BooleanField()
    reverse_relationship = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    relationship_concept = models.ForeignKey(Concept, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.relationship_id)


class ConceptSynonym(models.Model):
    """
    The CONCEPT_SYNONYM table is used to store alternate names and descriptions for Concepts.
    """
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE,
                                related_name='concept_synonym_concept')
    concept_synonym_name = models.CharField(max_length=1000)
    language_concept = models.ForeignKey(Concept, on_delete=models.SET_NULL, null=True, blank=True,
                                         related_name='concept_synonym_language_concept')

    def __str__(self):
        return str(self.id)


class ConceptAncestor(models.Model):
    """
    The CONCEPT_ANCESTOR table is designed to simplify observational analysis
    by providing the complete hierarchical relationships between Concepts.
    """
    ancestor_concept = models.ForeignKey(Concept, on_delete=models.SET_NULL, blank=True, null=True,
                                         related_name='concept_ancestor_ancestor_concept')
    descendant_concept = models.ForeignKey(Concept, on_delete=models.SET_NULL, blank=True, null=True,
                                           related_name='concept_ancestor_descendant_concept')
    min_levels_of_separation = models.IntegerField(null=True)
    max_levels_of_separation = models.IntegerField(null=True)

    def __str__(self):
        return str(self.id)


class SourceToConceptMap(models.Model):
    """
    The source to concept map table is a legacy data structure within the OMOP Common Data Model,
    recommended for use in ETL processes to maintain local source codes which are not available
    as Concepts in the Standardized Vocabularies
    """
    source_code = models.CharField(max_length=200, blank=True)
    source_concept = models.ForeignKey(Concept, on_delete=models.SET_NULL, blank=True, null=True,
                                       related_name='source_to_map_source_concept')
    source_vocabulary = models.ForeignKey('Vocabulary', on_delete=models.SET_NULL, blank=True, null=True,
                                          related_name='source_to_map_source_vocabulary')
    source_code_description = models.CharField(max_length=500, blank=True)
    target_concept = models.ForeignKey(Concept, on_delete=models.SET_NULL, blank=True, null=True,
                                       related_name='source_to_map_target_concept')
    target_vocabulary = models.ForeignKey('Vocabulary', on_delete=models.SET_NULL, blank=True, null=True,
                                          related_name='source_to_map_target_vocabulary')
    valid_start_date = models.DateField(null=True, blank=True)
    valid_end_date = models.DateField(null=True, blank=True)
    # D - deleted, U - updated
    invalid_reason = models.CharField(max_length=2, choices=[("D", "D"), ("U", "U")], blank=True, null=True)

    def __str__(self):
        return str(self.id)


class DrugStrength(models.Model):
    """
    The DRUG_STRENGTH table contains structured content about the amount or concentration and
    associated units of a specific ingredient contained within a particular drug product.
    """
    drug_concept = models.ForeignKey(Concept, on_delete=models.CASCADE,
                                     related_name='drug_strength_drug_concept')
    ingredient_concept = models.ForeignKey(Concept, on_delete=models.SET_NULL, blank=True, null=True,
                                           related_name='drug_strength_ingredient_concept')
    amount_value = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_unit_concept = models.ForeignKey(Concept, on_delete=models.SET_NULL, blank=True, null=True,
                                            related_name='drug_strength_amount_unit_concept')
    numerator_value = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    numerator_unit_concept = models.ForeignKey(Concept, on_delete=models.SET_NULL, blank=True, null=True,
                                               related_name='drug_strength_numerator_unit_concept')
    denominator_value = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    denominator_unit_concept = models.ForeignKey(Concept, on_delete=models.SET_NULL, blank=True, null=True,
                                                 related_name='drug_strength_denominator_unit_concept')
    box_size = models.IntegerField(blank=True, null=True)
    valid_start_date = models.DateField(null=True, blank=True)
    valid_end_date = models.DateField(null=True, blank=True)
    invalid_reason = models.CharField(max_length=2, choices=[("D", "D"), ("U", "U")], blank=True, null=True)

    def __str__(self):
        return str(self.id)


# Not found in documentation Tables but present in SQL statements


class Cohort(models.Model):
    """
    The COHORT table contains records of subjects that satisfy a given set of criteria for a duration of time.
    """
    cohort_definition = models.OneToOneField('CohortDefinition', on_delete=models.CASCADE)
    # TODO this probably should be M"M relationship to Person since Cohort might have many patients listed
    subject = models.ForeignKey('Person', on_delete=models.SET_NULL, blank=True, null=True)
    cohort_start_date = models.DateField(blank=True, null=True)
    cohort_end_date = models.DateField(blank=True, null=True)

    # TODO check this, it's not in the docs but in SQL statements
    # class Meta:
    # unique_together = (('cohort_definition', 'subject', 'cohort_start_date', 'cohort_end_date'),)

    def __str__(self):
        return str(self.id)


class CohortDefinition(models.Model):
    """
    The COHORT table contains records of subjects that satisfy a given set of criteria for a duration of time.
    """
    cohort_definition_id = models.CharField(primary_key=True, max_length=200)
    cohort_definition_name = models.CharField(max_length=255)
    cohort_definition_description = models.TextField(blank=True)
    definition_type_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                                related_name='cohort_definition_definition_type_concept')
    cohort_definition_syntax = models.TextField(blank=True)
    subject_concept = models.ForeignKey('Concept', on_delete=models.SET_NULL, blank=True, null=True,
                                        related_name='cohort_definition_subject_concept')
    cohort_initiation_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.cohort_definition_id)

