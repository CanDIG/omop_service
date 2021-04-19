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
    # person_obj.location = Location.objects.get(location_id=person["location_id"])
    # person_obj.provider = Provider.objects.get(provider_id=person["provider_id"])
    # person_obj.care_site = CareSite.objects.get(care_site_id=person["care_site_id"])
    person_obj.person_source_value = obj.get("person_source_value", None)
    person_obj.gender_source_value = obj.get("gender_source_value", None)
    person_obj.race_source_value = obj.get("race_source_value", None)
    person_obj.ethnicity_source_value = obj.get("ethnicity_source_value", None)
    person_obj.save()
    print(f"Person {person_obj.id} created.")


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
