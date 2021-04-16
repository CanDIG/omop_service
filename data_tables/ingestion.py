import csv
from .models import *


def ingest_persons(file):

    with open(f"{file}", "r") as f:
        records = csv.DictReader(f)
        for row in records:
            person = dict(row)
            person_obj, _ = Person.objects.get_or_create(
                person_id=person["person_id"]
            )
            # gender_concept = Concept.objects.get(concept_id=person["gender_concept_id"])
            person_obj.gender_concept = Concept.objects.get(concept_id=person["gender_concept_id"])
            person_obj.year_of_birth = person.get("year_of_birth", None)
            person_obj.month_of_birth = person.get("month_of_birth", None)
            person_obj.day_of_birth = person.get("day_of_birth", None)
            person_obj.birth_datetime = person.get("birth_datetime", None)

            # person_obj.death_datetime = person["death_datetime"]
            person_obj.race_concept = Concept.objects.get(concept_id=person["race_concept_id"])
            person_obj.ethnicity_concept = Concept.objects.get(concept_id=person["ethnicity_concept_id"])
            # person_obj.location = Location.objects.get(location_id=person["location_id"])
            # person_obj.provider = Provider.objects.get(provider_id=person["provider_id"])
            # person_obj.care_site = CareSite.objects.get(care_site_id=person["care_site_id"])
            person_obj.person_source_value = person.get("person_source_value", None)

            person_obj.gender_source_value = person.get("gender_source_value", None)
            person_obj.race_source_value = person.get("race_source_value", None)
            person_obj.ethnicity_source_value = person.get("ethnicity_source_value", None)
            person_obj.save()
            print(f"Person {person_obj.id} created.")