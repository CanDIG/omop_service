PERSON_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "person_id": {
            "type": "string"
        },
        "gender_concept": {
            "type": "string",
            "enum": [
                "FEMALE",
                "MALE"
            ]
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