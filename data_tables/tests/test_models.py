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
