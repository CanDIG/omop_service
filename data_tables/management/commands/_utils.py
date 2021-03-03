import csv
from data_tables.models import Concept, Domain, Vocabulary
import datetime


def parse_file(file):
    """ Parse the csv file and return dataframe. """

    with open(file, "r") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=",")
        headers = next(csv_data)
        df = [dict(zip(headers, i)) for i in csv_data]
        return df


def import_concepts(file):
    df = parse_file(file)
    for concept in df:
        valid_start_date = concept.get("valid_start_date", None)
        if valid_start_date:
            valid_start_date = datetime.datetime.strptime(valid_start_date, "%Y%m%d").date()
        valid_end_date = concept.get("valid_end_date", None)
        if valid_end_date:
            valid_end_date = datetime.datetime.strptime(valid_end_date, "%Y%m%d").date()
        created, _ = Concept.objects.get_or_create(
            concept_id=concept["concept_id"],
            concept_name=concept.get("concept_name", ""),
            standard_concept=concept.get("standard_concept", ""),
            concept_code=concept.get("concept_code", ""),
            valid_start_date=valid_start_date,
            valid_end_date=valid_end_date,
            invalid_reason=concept.get("invalid_reason", "")
        )
        print(f"Created {concept['concept_id']}.")


def import_vocabularies(file):
    df = parse_file(file)
    for vocab in df:
        created, _ = Vocabulary.objects.get_or_create(
            vocabulary_id=vocab["vocabulary_id"],
            vocabulary_name=vocab.get("vocabulary_name", ""),
            vocabulary_reference=vocab.get("vocabulary_reference", ""),
            vocabulary_version=vocab.get("vocabulary_version", "")
            #vocabulary_concept=vocab.get("vocabulary_concept", "")
        )
        print(f"Created {vocab['vocabulary_id']}.")


def import_domains(file):
    df = parse_file(file)
    for domain in df:
        created, _ = Domain.objects.get_or_create(
            domain_id=domain["domain_id"],
            domain_name=domain.get("domain_name", ""),
            #domain_concept=concept.get("domain_concept", ""),
        )
        print(f"Created {domain['domain_id']}.")
