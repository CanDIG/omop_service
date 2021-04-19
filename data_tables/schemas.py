PERSON_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "person_id": {
            "type": "string"
        },
        "gender_concept": {
            "type": "string"
        },
        "year_of_birth": {
            "type": "integer"
        },
        "month_of_birth": {
            "type": "integer"
        },
        "day_of_birth": {
            "type": "integer"
        },
        "birth_datetime": {
            "type": "string"
        },
        "death_datetime": {
            "type": "string"
        },
        "race_concept": {
            "type": "string"
        },
        "ethnicity_concept": {
            "type": "string"
        },
        "location": {
            "type": "string"
        },
        "provider": {
            "type": "string"
        },
        "care_site": {
            "type": "string"
        },
        "person_source_value": {
            "type": "string"
        },
        "gender_source_value": {
            "type": "string"
        },
        "gender_source_concept": {
            "type": "string"
        },
        "race_source_value": {
            "type": "string"
        },
        "race_source_concept": {
            "type": "string"
        },
        "ethnicity_source_value": {
            "type": "string"
        },
        "ethnicity_source_concept": {
            "type": "string"
        },
    },
    "required": ["person_id"]
}

OBSERVATION_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "observation_id": {
            "type": "string"
        },
        "person": {
            "type": "string"
        },
        "observation_concept": {
            "type": "string",
        },
        "observation_date": {
            "type": "string"
        },
        "observation_datetime": {
            "type": "string"
        },
        "observation_type_concept": {
            "type": "string"
        },
        "value_as_number": {
            "type": "number"
        },
        "value_as_string": {
            "type": "string"
        },
        "value_as_concept": {
            "type": "string"
        },
        "qualifier_concept": {
            "type": "string"
        },
        "unit_concept": {
            "type": "string"
        },
        "provider": {
            "type": "string"
        },
        "visit_occurrence": {
            "type": "string"
        },
        "visit_detail": {
            "type": "string"
        },
        "observation_source_value": {
            "type": "string"
        },
        "observation_source_concept": {
            "type": "string"
        },
        "unit_source_value": {
            "type": "string"
        },
        "qualifier_source_value": {
            "type": "string"
        },
        "observation_event": {
            "type": "string"
        },
        "obs_event_field_concept": {
            "type": "string"
        },
        "value_as_datetime": {
            "type": "string"
        },
    },
    "required": ["observation_id"]
}

OBSERVATION_PERIOD_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "observation_period_id": {
            "type": "string"
        },
        "person_id": {
            "type": "string"
        },
        "observation_period_start_date": {
            "type": "string"
        },
        "observation_period_end_date": {
            "type": "string"
        },
        "period_type_concept": {
            "type": "string"
        },
    },
    "required": ["observation_period_id"]
}

MEASUREMENT_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "measurement_id": {
            "type": "string"
        },
        "person": {
            "type": "string"
        },
        "measurement_concept": {
            "type": "string"
        },
        "measurement_date": {
            "type": "string"
        },
        "measurement_datetime": {
            "type": "string"
        },
        "measurement_type_concept": {
            "type": "string"
        },
        "operator_concept": {
            "type": "string"
        },
        "value_as_number": {
            "type": "number"
        },
        "value_as_concept": {
            "type": "string"
        },
        "unit_concept": {
            "type": "string"
        },
        "range_low": {
            "type": "number"
        },
        "range_high": {
            "type": "number"
        },
        "provider": {
            "type": "string"
        },
        "visit_occurrence": {
            "type": "string"
        },
        "visit_detail": {
            "type": "string"
        },
        "measurement_source_value": {
            "type": "string"
        },
        "measurement_source_concept": {
            "type": "string"
        },
        "unit_source_value": {
            "type": "string"
        },
        "value_source_value": {
            "type": "string"
        },
    },
    "required": ["measurement_id"]
}

CONDITION_OCCURRENCE_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "condition_occurrence_id": {
            "type": "string"
        },
        "person": {
            "type": "string"
        },
        "condition_concept": {
            "type": "string"
        },
        "condition_start_date": {
            "type": "string"
        },
        "condition_start_datetime": {
            "type": "string"
        },
        "condition_end_date": {
            "type": "string"
        },
        "condition_end_datetime": {
            "type": "string"
        },
        "condition_type_concept": {
            "type": "string"
        },
        "condition_status_concept": {
            "type": "string"
        },
        "stop_reason": {
            "type": "string"
        },
        "provider": {
            "type": "string"
        },
        "visit_occurrence": {
            "type": "string"
        },
        "visit_detail": {
            "type": "string"
        },
        "condition_source_value": {
            "type": "string"
        },
        "condition_source_concept": {
            "type": "string"
        },
        "condition_status_source_value": {
            "type": "string"
        },
    },
    "required": ["condition_occurrence_id"]
}

SPECIMEN_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "specimen_id": {
            "type": "string"
        },
        "person": {
            "type": "string"
        },
        "specimen_concept": {
            "type": "string"
        },
        "specimen_type_concept": {
            "type": "string"
        },
        "specimen_date": {
            "type": "string"
        },
        "specimen_datetime": {
            "type": "string"
        },
        "quantity": {
            "type": "number"
        },
        "unit_concept": {
            "type": "string"
        },
        "anatomic_site_concept": {
            "type": "string"
        },
        "disease_status_concept": {
            "type": "string"
        },
        "specimen_source_id": {
            "type": "string"
        },
        "specimen_source_value": {
            "type": "string"
        },
        "unit_source_value": {
            "type": "string"
        },
        "anatomic_site_source_value": {
            "type": "string"
        },
        "disease_status_source_value": {
            "type": "string"
        }
    },
    "required": ["specimen_id"]
}
