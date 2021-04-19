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
    observation_obj, _ = Observation.objects.get_or_create(observation_id=obj["observation_id"])
    observation_obj.person = Person.objects.get(person_id=obj["person_id"])
    observation_obj.observation_concept = Concept.objects.get(concept_id=obj["observation_concept_id"])
    observation_obj.observation_date = obj.get("observation_date", None)
    observation_obj.observation_datetime = obj.get("observation_datetime", None)
    observation_obj.value_as_number = obj.get("value_as_number", None)
    observation_obj.value_as_string = obj.get("value_as_string", None)

    concept_fields = {
        "observation_type_concept_id": observation_obj.observation_type_concept,
        "value_as_concept_id": observation_obj.value_as_concept,
        "qualifier_concept_id": observation_obj.qualifier_concept,
        "unit_concept_id": observation_obj.unit_concept,
        "observation_source_concept_id": observation_obj.observation_source_concept
    }
    for value in concept_fields.keys():
        if obj[value] and obj[value] != "":
            concept_fields[value] = Concept.objects.get(concept_id=obj[value])

    # FKs
    # observation_obj.provider = Provider.objects.get(provider_id=person["provider_id"])
    # observation_obj.visit_occurrence = VisitOccurrence.objects.get(visit_occurrence_id=person["visit_occurrence_id"])
    # observation_obj.visit_detail = VisitDetail.objects.get(visit_detail_id=person["visit_detail_id"])

    observation_obj.observation_source_value = obj.get("observation_source_value", None)
    observation_obj.unit_source_value = obj.get("unit_source_value", None)
    observation_obj.qualifier_source_value = obj.get("qualifier_source_value", None)
    # FK
    # observation_obj.observation_event = ProcedureOccurrence.objects.get(
    #     procedure_occurrence_id=obj["observation_event_id"]
    # )
    # if obj["obs_event_field_concept_id"] and obj["obs_event_field_concept_id"] != "":
    #     observation_obj.obs_event_field_concept = Concept.objects.get(concept_id=obj["obs_event_field_concept_id"])

    observation_obj.value_as_datetime = obj.get("value_as_datetime", None)
    print(f"Observation {observation_obj.id} created.")


def ingest_persons(file):
    file_type = file.split(".")[-1]

    if file_type == "csv":
        with open(f"{file}", "r") as file_in:
            records = csv.DictReader(file_in)
            for row in records:
                create_person(dict(row))

    elif file_type == "json":
        with open(f"{file}") as file_in:
            records = json.load(file_in)
            for record in records:
                create_person(record)

    else:
        raise IngestError(f"The file format is not supported: {file_type}")
