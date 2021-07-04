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
