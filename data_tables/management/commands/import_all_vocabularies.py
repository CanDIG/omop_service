from django.core.management.base import BaseCommand
from ._utils import *


# Default file names correspond to the file names provided by Athena server
DEFAULT_FILENAMES = {
    "vocabulary": "VOCABULARY.csv",
    "domain": "DOMAIN.csv",
    "concept_class": "CONCEPT_CLASS.csv",
    "concept": "CONCEPT.csv",
    "concept_ancestor": "CONCEPT_ANCESTOR.csv",
    "relationship": "RELATIONSHIP.csv",
    "concept_relationship": "CONCEPT_RELATIONSHIP.csv",
    "concept_synonym": "CONCEPT_SYNONYM.csv"
}


class Command(BaseCommand):
    """ run: python manage.py import_all_vocabularies """

    help = "Imports all standartized vocabularies files obtained from the Athena server."

    def add_arguments(self, parser):
        parser.add_argument("--vocabulary", type=str, help="The vocabulary filename to import.")
        parser.add_argument("--domain", type=str, help="The domain filename to import.")
        parser.add_argument("--concept_class", type=str, help="The concept class filename to import.")
        parser.add_argument("--concept", type=str, help="The concept filename to import.")
        parser.add_argument("--concept_ancestor", type=str, help="The concept ancestor filename to import.")
        parser.add_argument("--relationship", type=str, help="The relationship filename to import.")
        parser.add_argument("--concept_relationship", type=str, help="The concept relationship filename to import.")
        parser.add_argument("--concept_synonym", type=str, help="The concept synonym filename to import.")

    def _required_import(self, value, function, **options):
        try:
            if options[value]:
                function(options[value])
            else:
                function(DEFAULT_FILENAMES[value])
            self.stdout.write(self.style.SUCCESS(f"Successfully imported {value}"))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR("The file is not found"))
            exit()

    def handle(self, *args, **options):

        # required vocabularies
        for value, function in zip(["vocabulary", "domain", "concept_class"],
                                   [import_vocabulary, import_domain, import_concept_class]):
            self._required_import(value, function, **options)
