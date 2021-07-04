VALID_CONCEPT_DOMAIN_GENDER = {
    "concept_id": "2",
    "concept_name": "Gender",
    "concept_code": "OMOP generated",
}


def valid_domain_gender(domain_concept):
    return {
        "domain_id": "Gender",
        "domain_name": "Gender",
        "domain_concept": domain_concept
    }


VALID_VOCABULARY_GENDER = {
    "vocabulary_id": "Gender",
    "vocabulary_name": "OMOP Gender",
    "vocabulary_reference": "OMOP generated"
}

VALID_CONCEPT_CLASS_GENDER = {
    "concept_class_id": "Gender",
    "concept_class_name": "Gender"
}

VALID_CONCEPT_NONE = {
    "concept_id": "0",
    "concept_name": "No matching concept",
    "concept_code": "No matching concept"
}


def valid_concept_female(domain, vocabulary, concept_class):
    return {
        "concept_id": "8532",
        "concept_name": "FEMALE",
        "domain_id": domain,
        "vocabulary_id": vocabulary,
        "concept_class_id": concept_class,
        "standard_concept": "S",
        "concept_code": "F"
    }


def valid_person(concept_female, concept_none):
    return {
        "person_id": "1",
        "gender_concept_id": concept_female,
        "year_of_birth": 2000,
        "month_of_birth": 7,
        "day_of_birth": 5,
        "birth_datetime": "2000-07-05 00:00:00",
        "race_concept_id": concept_none,
        "ethnicity_concept_id": concept_none,
        "person_source_value": "0004bbbd-1e41-42b0-bd6e-fece53cc1817",
        "gender_source_value": "F",
        "gender_source_concept_id": concept_none,
        "race_source_value": "white",
        "race_source_concept_id": concept_none,
        "ethnicity_source_value": "nonhispanic",
        "ethnicity_source_concept_id": concept_none
    }
