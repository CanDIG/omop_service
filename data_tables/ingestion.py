import csv
import json
from .models import *


class IngestError(Exception):
    pass


def create_person(obj):
    person_obj, _ = Person.objects.get_or_create(person_id=obj["person_id"])
    person_obj.gender_concept = Concept.objects.get(concept_id=obj["gender_concept_id"])
    person_obj.year_of_birth = obj.get("year_of_birth", None)
    person_obj.month_of_birth = obj.get("month_of_birth", None)
    person_obj.day_of_birth = obj.get("day_of_birth", None)
    person_obj.birth_datetime = obj.get("birth_datetime", None)
    if obj["death_datetime"] and obj["death_datetime"] != "":
        person_obj.death_datetime = obj["death_datetime"]
    person_obj.race_concept = Concept.objects.get(concept_id=obj["race_concept_id"])
    person_obj.ethnicity_concept = Concept.objects.get(concept_id=obj["ethnicity_concept_id"])

    # FKs
    # person_obj.location = Location.objects.get(location_id=person["location_id"])
    # person_obj.provider = Provider.objects.get(provider_id=person["provider_id"])
    # person_obj.care_site = CareSite.objects.get(care_site_id=person["care_site_id"])

    person_obj.person_source_value = obj.get("person_source_value", None)
    person_obj.gender_source_value = obj.get("gender_source_value", None)
    person_obj.race_source_value = obj.get("race_source_value", None)
    person_obj.ethnicity_source_value = obj.get("ethnicity_source_value", None)
    person_obj.save()
    print(f"Person {person_obj.id} created.")


def create_observation(obj):
    person = Person.objects.get(person_id=obj["person_id"])
    observation_obj = Observation(observation_id=obj["observation_id"], person=person)
    observation_obj.observation_concept = Concept.objects.get(concept_id=obj["observation_concept_id"])

    concept_fields = {
        "observation_type_concept_id": None,
        "value_as_concept_id": None,
        "qualifier_concept_id": None,
        "unit_concept_id": None,
        "observation_source_concept_id": None
    }
    for value in concept_fields.keys():
        if value in obj and obj[value] != "":
            concept_fields[value] = Concept.objects.get(concept_id=obj[value])

    observation_obj.observation_type_concept = concept_fields["observation_type_concept_id"]
    observation_obj.value_as_concept = concept_fields["value_as_concept_id"]
    observation_obj.qualifier_concept = concept_fields["qualifier_concept_id"]
    observation_obj.unit_concept = concept_fields["unit_concept_id"]
    observation_obj.observation_source_concept = concept_fields["observation_source_concept_id"]

    text_fields = ["observation_date", "observation_datetime", "value_as_number", "value_as_string",
                   "observation_source_value", "unit_source_value", "qualifier_source_value", "value_as_datetime"]
    for field in text_fields:
        if field in obj and obj[field] != "":
            observation_obj.__dict__[field] = obj[field]

    # FKs
    # observation_obj.provider = Provider.objects.get(provider_id=person["provider_id"])
    # observation_obj.visit_occurrence = VisitOccurrence.objects.get(visit_occurrence_id=person["visit_occurrence_id"])
    # observation_obj.visit_detail = VisitDetail.objects.get(visit_detail_id=person["visit_detail_id"])

    # FK
    # observation_obj.observation_event = ProcedureOccurrence.objects.get(
    #     procedure_occurrence_id=obj["observation_event_id"]
    # )
    # if obj["obs_event_field_concept_id"] and obj["obs_event_field_concept_id"] != "":
    #     observation_obj.obs_event_field_concept = Concept.objects.get(concept_id=obj["obs_event_field_concept_id"])

    observation_obj.save()
    print(f"Observation {observation_obj.id} created.")


def create_condition_occurence(obj):
    person = Person.objects.get(person_id=obj["person_id"])
    condition_occ_obj = ConditionOccurrence(condition_occurrence_id=obj["condition_occurrence_id"], person=person)
    condition_occ_obj.condition_concept = Concept.objects.get(concept_id=obj["condition_concept_id"])
    text_fields = ["condition_start_date", "condition_start_datetime", "condition_end_date", "condition_end_datetime",
                   "stop_reason", "condition_source_value", "condition_status_source_value"]
    for field in text_fields:
        if field in obj and obj[field] != "":
            condition_occ_obj.__dict__[field] = obj[field]
    condition_occ_obj.condition_type_concept = Concept.objects.get(concept_id=obj["condition_type_concept_id"])

    # FKs
    # condition_occ_obj.provider = Provider.objects.get(provider_id=obj["provider_id"])
    # condition_occ_obj.visit_occurrence = VisitOccurrence.objects.get(visit_occurrence_id=obj["visit_occurrence_id"])
    # condition_occ_obj.visit_detail = VisitDetail.objects.get(visit_detail_id=obj["visit_detail_id"])

    condition_occ_obj.condition_source_concept = Concept.objects.get(concept_id=obj["condition_source_concept_id"])
    condition_occ_obj.save()
    print(f"Condition occurrence {condition_occ_obj.id} created.")


def create_measurement(obj):
    person = Person.objects.get(person_id=obj["person_id"])
    measurement_obj = Measurement(measurement_id=obj["measurement_id"], person=person)
    measurement_obj.measurement_concept = Concept.objects.get(concept_id=obj["measurement_concept_id"])
    # TODO the rest of the fields
    measurement_obj.measurement_type_concept = Concept.objects.get(concept_id=obj["measurement_type_concept_id"])
    measurement_obj.save()
    print(f"Measurement {measurement_obj.id} created.")


def ingest_generic(file, data_type):
    file_type = file.split(".")[-1]

    datatypes = {
        "person": create_person,
        "observation": create_observation,
        "condition_occurrence": create_condition_occurence,
        "measurement": create_measurement
    }

    if file_type == "csv":
        with open(f"{file}", "r") as file_in:
            records = csv.DictReader(file_in)
            for row in records:
                datatypes[data_type](dict(row))

    elif file_type == "json":
        with open(f"{file}") as file_in:
            records = json.load(file_in)
            for record in records:
                datatypes[data_type](record)

    else:
        raise IngestError(f"The file format is not supported: {file_type}")
