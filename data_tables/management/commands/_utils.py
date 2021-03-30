from django.db import connection
import csv
from data_tables.models import (
    Concept, Domain, Vocabulary,
    ConceptClass, ConceptAncestor,
    Relationship, ConceptRelationship,
    ConceptSynonym
)
import datetime


def parse_file(file):
    """ Parse the csv file and return dataframe. """

    with open(file, "r", encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter="\t")  # or ","
        headers = next(csv_data)
        df = [dict(zip(headers, i)) for i in csv_data]
        return df


def import_vocabulary(file):
    df = parse_file(file)
    for vocab in df:
        concept, _ = Concept.objects.get_or_create(concept_id=vocab["vocabulary_concept_id"])
        vocabulary_obj, _ = Vocabulary.objects.get_or_create(
            vocabulary_id=vocab["vocabulary_id"],
            vocabulary_name=vocab.get("vocabulary_name", ""),
            vocabulary_reference=vocab.get("vocabulary_reference", ""),
            vocabulary_version=vocab.get("vocabulary_version", ""),
            vocabulary_concept=concept
        )
        print(f"Created vocabulary {vocab['vocabulary_id']}")


def import_domain(file):
    df = parse_file(file)
    for domain in df:
        concept, _ = Concept.objects.get_or_create(concept_id=domain["domain_concept_id"])
        domain_obj, _ = Domain.objects.get_or_create(
            domain_id=domain["domain_id"],
            domain_name=domain.get("domain_name", ""),
            domain_concept=concept
        )
        print(f"Created domain {domain['domain_id']}")


def import_concept_class(file):
    df = parse_file(file)
    for concept_class in df:
        concept, _ = Concept.objects.get_or_create(concept_id=concept_class["concept_class_concept_id"])
        concept_class_obj, _ = ConceptClass.objects.get_or_create(
            concept_class_id=concept_class["concept_class_id"],
            concept_class_name=concept_class.get("concept_class_name", ""),
            concept_class_concept=concept
        )
        print(f"Created concept class {concept_class['concept_class_id']}")


def import_concept(file):
    df = parse_file(file)
    for concept in df:

        # convert date strings to datetime.date object
        dates = dict()
        for d in ["valid_start_date", "valid_end_date"]:
            if concept[d]:
                dates[d] = datetime.datetime.strptime(concept[d], "%Y%m%d").date()

        # for now those should be created beforehand
        # domain
        domain, _ = Domain.objects.get_or_create(domain_id=concept["domain_id"])
        # vocabulary
        vocabulary, _ = Vocabulary.objects.get_or_create(vocabulary_id=concept["vocabulary_id"])
        # concept-class
        concept_class, _ = ConceptClass.objects.get_or_create(concept_class_id=concept["concept_class_id"])

        concept_obj, _ = Concept.objects.get_or_create(
            concept_id=concept["concept_id"]
        )
        concept_obj.concept_name = concept.get("concept_name", "")
        concept_obj.domain = domain
        concept_obj.vocabulary = vocabulary
        concept_obj.concept_class = concept_class
        concept_obj.standard_concept = concept.get("standard_concept", "")
        concept_obj.concept_code = concept.get("concept_code", "")
        concept_obj.valid_start_date = dates["valid_start_date"]
        concept_obj.valid_end_date = dates["valid_end_date"]
        concept_obj.invalid_reason = concept.get("invalid_reason", "")
        concept_obj.save()
        print(f"Created concept {concept['concept_id']}")


def import_concept_ancestor(file):
    df = parse_file(file)
    for concept_ancestor in df:
        ancestor_concept, _ = Concept.objects.get_or_create(concept_id=concept_ancestor["ancestor_concept_id"])
        descendant_concept, _ = Concept.objects.get_or_create(concept_id=concept_ancestor["descendant_concept_id"])
        concept_ancestor_obj, _ = ConceptAncestor.objects.get_or_create(
            ancestor_concept=ancestor_concept,
            descendant_concept=descendant_concept,
            min_levels_of_separation=concept_ancestor.get("min_levels_of_separation"),
            max_levels_of_separation=concept_ancestor.get("max_levels_of_separation")
        )
        print(f"Created concept ancestor {concept_ancestor_obj.id}")


def import_relationship(file):
    df = parse_file(file)
    for relationship in df:
        relationship_concept, _ = Concept.objects.get_or_create(concept_id=relationship["relationship_concept_id"])
        is_hierarchical = True if relationship["is_hierarchical"] == "1" else False
        defines_ancestry = True if relationship["defines_ancestry"] == "1" else False
        relationship_obj, _ = Relationship.objects.get_or_create(
            relationship_id=relationship["relationship_id"],
            relationship_name=relationship.get("relationship_name"),
            is_hierarchical=is_hierarchical,
            defines_ancestry=defines_ancestry,
            relationship_concept=relationship_concept
        )
        print(f"Created relationship {relationship_obj}")

    # update Relationship object with reverse relationship to its class
    for relationship in df:
        reverse_relationship = Relationship.objects.get(
            relationship_id=relationship["reverse_relationship_id"],
        )
        relationship_obj = Relationship.objects.get(
            relationship_id=relationship["relationship_id"]
        )
        relationship_obj.reverse_relationship = reverse_relationship
        relationship_obj.save()
        print(f"Linked reversed relationship to {relationship_obj}")


def import_concept_relationship(file):
    df = parse_file(file)
    for concept_relationship in df:
        concept_id_1, _ = Concept.objects.get_or_create(concept_id=concept_relationship["concept_id_1"])
        concept_id_2, _ = Concept.objects.get_or_create(concept_id=concept_relationship["concept_id_2"])
        relationship, _ = Relationship.objects.get_or_create(relationship_id=concept_relationship["relationship_id"])

        # convert date strings to datetime.date object
        dates = dict()
        for d in ["valid_start_date", "valid_end_date"]:
            if concept_relationship[d]:
                dates[d] = datetime.datetime.strptime(concept_relationship[d], "%Y%m%d").date()

        concept_relationship_obj, _ = ConceptRelationship.objects.get_or_create(
            concept_id_1=concept_id_1,
            concept_id_2=concept_id_2,
            relationship=relationship,
            valid_start_date=dates.get("valid_start_date"),
            valid_end_date=dates.get("valid_end_date"),
            invalid_reason=concept_relationship.get("invalid_reason")
        )
        print(f"Created concept relationship {concept_relationship_obj}")


def import_concept_synonym(file):
    df = parse_file(file)
    for concept_synonym in df:
        concept, _ = Concept.objects.get_or_create(concept_id=concept_synonym["concept_id"])
        language_concept, _ = Concept.objects.get_or_create(concept_id=concept_synonym["language_concept_id"])
        concept_synonym_obj, _ = ConceptSynonym.objects.get_or_create(
            concept=concept,
            concept_synonym_name=concept_synonym["concept_synonym_name"],
            language_concept=language_concept
        )
        print(f"Created concept synonym {concept_synonym_obj.concept_synonym_name}")


#TODO better location
def import_postgres():
    with connection.cursor() as cursor:
        cursor.execute("""
        COPY public.data_tables_concept(concept_id, concept_name, domain_id, vocabulary_id, concept_class_id, standard_concept, concept_code, valid_start_date, valid_end_date, invalid_reason)
        FROM 'C:\CDMV6VOCAB\CONCEPT.csv'
        WITH DELIMITER E'\t'
        CSV HEADER QUOTE E'\b' ;
        
        COPY public.data_tables_conceptrelationship(concept_id_1, concept_id_2, relationship_id, valid_start_date, valid_end_date, invalid_reason)
        FROM 'C:\CDMV6VOCAB\CONCEPT_RELATIONSHIP.csv'
        WITH DELIMITER E'\t'
        CSV HEADER QUOTE E'\b' ;
        
        COPY public.data_tables_conceptancestor(ancestor_concept_id, descendant_concept_id, min_levels_of_separation, max_levels_of_separation)
        FROM 'C:\CDMV6VOCAB\CONCEPT_ANCESTOR.csv'
        WITH DELIMITER E'\t'
        CSV HEADER QUOTE E'\b' ;
        
        COPY public.data_tables_conceptsynonym(concept_id, concept_synonym_name, language_concept_id)
        FROM 'C:\CDMV6VOCAB\CONCEPT_SYNONYM.csv'
        WITH DELIMITER E'\t'
        CSV HEADER QUOTE E'\b' ;

        COPY public.data_tables_vocabulary(vocabulary_id, vocabulary_name, vocabulary_reference, vocabulary_version, vocabulary_concept_id)
        FROM 'C:\CDMV6VOCAB\VOCABULARY.csv'
        WITH DELIMITER E'\t'
        CSV HEADER QUOTE E'\b' ;
        
        COPY public.data_tables_relationship(relationship_id, relationship_name, is_hierarchical, defines_ancestry, reverse_relationship_id, relationship_concept_id)
        FROM 'C:\CDMV6VOCAB\RELATIONSHIP.csv'
        WITH DELIMITER E'\t'
        CSV HEADER QUOTE E'\b' ;

        COPY public.data_tables_conceptclass(concept_class_id, concept_class_name, concept_class_concept_id)
        FROM 'C:\CDMV6VOCAB\CONCEPT_CLASS.csv'
        WITH DELIMITER E'\t'
        CSV HEADER QUOTE E'\b' ;

        COPY public.data_tables_domain(domain_id, domain_name, domain_concept_id)
        FROM 'C:\CDMV6VOCAB\DOMAIN.csv'
        WITH DELIMITER E'\t'
        CSV HEADER QUOTE E'\b' ;
        """)

    return
