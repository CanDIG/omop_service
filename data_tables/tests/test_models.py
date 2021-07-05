from datetime import datetime

from django.test import TestCase
from .constants import *
from ..models import *


class ConceptTest(TestCase):
    """ Test module for Concept model """

    def setUp(self):
        self.concept_domain_gender = Concept.objects.create(**VALID_CONCEPT_DOMAIN_GENDER)
        self.domain_gender = Domain.objects.create(**valid_domain_gender(self.concept_domain_gender))
        self.vocabulary_gender = Vocabulary.objects.create(**VALID_VOCABULARY_GENDER)
        self.concept_class_gender = ConceptClass.objects.create(**VALID_CONCEPT_CLASS_GENDER)
        self.concept_none = Concept.objects.create(**VALID_CONCEPT_NONE)
        self.concept_female = Concept.objects.create(
            **valid_concept_female(
                domain=self.domain_gender,
                vocabulary=self.vocabulary_gender,
                concept_class=self.concept_class_gender
            )
        )

    def test_concept(self):
        self.assertEqual(3, Concept.objects.all().count())
        concept_ids = ["2", "0", "8532"]
        database_concept_ids = [c["concept_id"] for c in Concept.objects.values("concept_id")]
        self.assertEqual(set(concept_ids), set(database_concept_ids))
        database_concept_names = [c["concept_name"] for c in Concept.objects.values("concept_name")]
        self.assertIn("FEMALE", database_concept_names)
        self.assertIn("Gender", database_concept_names)
        self.assertIn("No matching concept", database_concept_names)


class PersonTest(TestCase):
    """ Test module for Person class """

    def setUp(self):
        self.concept_domain_gender = Concept.objects.create(**VALID_CONCEPT_DOMAIN_GENDER)
        self.domain_gender = Domain.objects.create(**valid_domain_gender(self.concept_domain_gender))
        self.vocabulary_gender = Vocabulary.objects.create(**VALID_VOCABULARY_GENDER)
        self.concept_class_gender = ConceptClass.objects.create(**VALID_CONCEPT_CLASS_GENDER)
        self.concept_none = Concept.objects.create(**VALID_CONCEPT_NONE)
        self.concept_female = Concept.objects.create(
            **valid_concept_female(
                domain=self.domain_gender,
                vocabulary=self.vocabulary_gender,
                concept_class=self.concept_class_gender
            )
        )
        self.person = Person.objects.create(**valid_person(concept_female=self.concept_female,
                                                           concept_none=self.concept_none))

    def test_person(self):
        # print(Person.objects.get(person_id="1").__dict__)
        concept_none = Concept.objects.get(concept_id="0").concept_id
        self.assertEqual(1, Person.objects.all().count())
        self.assertEqual("8532", Person.objects.get(person_id="1").gender_concept_id)
        self.assertEqual(2000, Person.objects.get(person_id="1").year_of_birth)
        self.assertEqual(7, Person.objects.get(person_id="1").month_of_birth)
        self.assertEqual(5, Person.objects.get(person_id="1").day_of_birth)
        self.assertIsNotNone(Person.objects.get(person_id="1").birth_datetime)
        self.assertEqual(concept_none, Person.objects.get(person_id="1").race_concept_id)
        self.assertEqual(concept_none, Person.objects.get(person_id="1").ethnicity_concept_id)
        self.assertEqual("0004bbbd-1e41-42b0-bd6e-fece53cc1817", Person.objects.get(person_id="1").person_source_value)
        self.assertEqual("F", Person.objects.get(person_id="1").gender_source_value)
        self.assertEqual(concept_none, Person.objects.get(person_id="1").gender_source_concept_id)
        self.assertEqual("white", Person.objects.get(person_id="1").race_source_value)
        self.assertEqual(concept_none, Person.objects.get(person_id="1").race_source_concept_id)
        self.assertEqual("nonhispanic", Person.objects.get(person_id="1").ethnicity_source_value)
        self.assertEqual(concept_none, Person.objects.get(person_id="1").ethnicity_source_concept_id)


# Set up test data for the rest of the tests
class GenericTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        """ Load initial data for all GenericTestCases """

        # set up database with one Person
        cls.concept_domain_gender = Concept.objects.create(**VALID_CONCEPT_DOMAIN_GENDER)
        cls.domain_gender = Domain.objects.create(**valid_domain_gender(cls.concept_domain_gender))
        cls.vocabulary_gender = Vocabulary.objects.create(**VALID_VOCABULARY_GENDER)
        cls.concept_class_gender = ConceptClass.objects.create(**VALID_CONCEPT_CLASS_GENDER)
        cls.concept_none = Concept.objects.create(**VALID_CONCEPT_NONE)
        cls.concept_female = Concept.objects.create(
            **valid_concept_female(
                domain=cls.domain_gender,
                vocabulary=cls.vocabulary_gender,
                concept_class=cls.concept_class_gender
            )
        )
        cls.person = Person.objects.create(**valid_person(concept_female=cls.concept_female,
                                                          concept_none=cls.concept_none))
        # for Observation
        cls.observation_concept = Concept.objects.create(concept_id="38000276", concept_name="Problem list from EHR")
        cls.observation_source_concept = Concept.objects.create(
            concept_id="40481087", concept_name="Viral sinusitis"
        )
        cls.observation = Observation.objects.create(**valid_observation(
            cls.person.id, cls.observation_concept, cls.concept_none.concept_id, cls.observation_source_concept))

        # for Condition Occurence
        cls.condition_concept = Concept.objects.create(concept_id="260139", concept_name="Acute bronchitis")
        cls.condition_type_concept = Concept.objects.create(
            concept_id="32020", concept_name="EHR encounter diagnosis"
        )
        cls.condition_occurrence = ConditionOccurrence.objects.create(**valid_condition_occurrence(
            cls.person.id, cls.condition_concept, cls.condition_type_concept, cls.concept_none.concept_id))

        # for Measurement
        cls.measurement_concept = Concept.objects.create(concept_id="4024958", concept_name="Throat culture")
        cls.measurement_type_concept = Concept.objects.create(
            concept_id="5001", concept_name="Test ordered through EHR"
        )
        cls.measurement = Measurement.objects.create(**valid_measurement(
            cls.person, cls.measurement_concept, cls.measurement_type_concept, cls.concept_none.concept_id))

    def test_person(self):
        self.assertEqual(1, Person.objects.all().count())

    def test_observation(self):
        concept_none = Concept.objects.get(concept_id="0").concept_id
        self.assertEqual(1, Observation.objects.all().count())
        observation = Observation.objects.get(observation_id="1")
        self.assertEqual(concept_none, observation.observation_concept_id)
        self.assertEqual(datetime.strptime("2019-08-29", "%Y-%m-%d").date(), observation.observation_date)
        self.assertEqual("38000276", observation.observation_type_concept_id)
        self.assertEqual(1.5, observation.value_as_number)
        self.assertEqual("test value", observation.value_as_string)
        self.assertEqual(concept_none, observation.value_as_concept_id)
        self.assertEqual(concept_none, observation.qualifier_concept_id)
        self.assertEqual(concept_none, observation.unit_concept_id)
        self.assertEqual("444814009", observation.observation_source_value)
        self.assertEqual("40481087", observation.observation_source_concept_id)
        self.assertEqual("unit test value", observation.unit_source_value)
        self.assertEqual("qualifier test value", observation.qualifier_source_value)
        self.assertEqual(self.person, observation.person)
        self.assertEqual("Viral sinusitis", observation.observation_source_concept.concept_name)

    def test_condition_occurrence(self):
        concept_none = Concept.objects.get(concept_id="0").concept_id
        self.assertEqual(1, ConditionOccurrence.objects.all().count())
        condition_occurrence = ConditionOccurrence.objects.get(condition_occurrence_id="1")
        self.assertEqual(self.person, condition_occurrence.person)
        self.assertEqual(Concept.objects.get(concept_name="Acute bronchitis").concept_id,
                         condition_occurrence.condition_concept_id)
        self.assertEqual(datetime.strptime("2017-06-05", "%Y-%m-%d").date(), condition_occurrence.condition_start_date)
        self.assertEqual(datetime.strptime("2017-06-12", "%Y-%m-%d").date(), condition_occurrence.condition_end_date)
        self.assertEqual(Concept.objects.get(concept_name="EHR encounter diagnosis").concept_id,
                         condition_occurrence.condition_type_concept_id)
        self.assertEqual("test stop reason", condition_occurrence.stop_reason)
        self.assertEqual("195662009", condition_occurrence.condition_source_value)
        self.assertEqual(concept_none, condition_occurrence.condition_source_concept_id)
        self.assertEqual("unknown", condition_occurrence.condition_status_source_value)

    def test_measurement(self):
        concept_none = Concept.objects.get(concept_id="0").concept_id
        self.assertEqual(1, Measurement.objects.all().count())
        measurement = Measurement.objects.get(measurement_id="1")
        self.assertEqual(self.person, measurement.person)
        self.assertEqual(Concept.objects.get(concept_name="Throat culture").concept_id,
                         measurement.measurement_concept_id)
        self.assertEqual(datetime.strptime("2017-06-05", "%Y-%m-%d").date(), measurement.measurement_date)
        self.assertEqual(Concept.objects.get(concept_name="Test ordered through EHR").concept_id,
                         measurement.measurement_type_concept_id)
        self.assertEqual(concept_none, measurement.operator_concept_id)
        self.assertEqual(1.5, measurement.value_as_number)
        self.assertEqual(concept_none, measurement.value_as_concept_id)
        self.assertEqual(concept_none, measurement.unit_concept_id)
        self.assertEqual("117015009", measurement.measurement_source_value)
        self.assertEqual(concept_none, measurement.measurement_source_concept_id)
        self.assertEqual("test unit source value", measurement.unit_source_value)
        self.assertEqual("test value source value", measurement.value_source_value)
