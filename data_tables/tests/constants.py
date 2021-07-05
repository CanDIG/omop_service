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


# PERSON
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


# OBSERVATION
def valid_observation(person, observation_concept, concept_none, observation_source_concept):
    return {
        "observation_id": "1",
        "person_id": person,
        "observation_concept_id": concept_none,
        "observation_date": "2019-08-29",
        "observation_type_concept_id": observation_concept,
        "value_as_number": 1.5,
        "value_as_string": "test value",
        "value_as_concept_id": concept_none,
        "qualifier_concept_id": concept_none,
        "unit_concept_id": concept_none,
        "observation_source_value": "444814009",
        "observation_source_concept_id": observation_source_concept,
        "unit_source_value": "unit test value",
        "qualifier_source_value": "qualifier test value"
    }


# CONDITION OCCURENCE
def valid_condition_occurrence(person, condition_concept, condition_type_concept, concept_none):
    return {
        "condition_occurrence_id": "1",
        "person_id": person,
        "condition_concept_id": condition_concept,
        "condition_start_date": "2017-06-05",
        # TODO datetime tests
        # "condition_start_datetime": "2017-06-05 00:00:00",
        "condition_end_date": "2017-06-12",
        # "condition_end_datetime": "2017-06-12 00:00:00",
        "condition_type_concept_id": condition_type_concept,
        "stop_reason": "test stop reason",
        # "provider_id": "",
        # "visit_occurrence_id": "7",
        # "visit_detail_id": "0",
        "condition_source_value": "195662009",
        "condition_source_concept_id": concept_none,
        "condition_status_source_value": "unknown"
    }


# MEASUREMENT
def valid_measurement(person, measurement_concept, measurement_type_concept, concept_none):
    return {
        "measurement_id": "1",
        "person": person,
        "measurement_concept_id": measurement_concept,
        "measurement_date": "2017-06-05",
        # TODO datetime tests
        # "measurement_datetime": "2017-06-05 00:00:00",
        "measurement_type_concept_id": measurement_type_concept,
        "operator_concept_id": concept_none,
        "value_as_number": 1.5,
        "value_as_concept_id": concept_none,
        "unit_concept_id": concept_none,
        "range_low": 2.1,
        "range_high": 2.9,
        # "provider": "",
        # "visit_occurrence": "7",
        # "visit_detail": "0",
        "measurement_source_value": "117015009",
        "measurement_source_concept_id": concept_none,
        "unit_source_value": "test unit source value",
        "value_source_value": "test value source value"
    }
