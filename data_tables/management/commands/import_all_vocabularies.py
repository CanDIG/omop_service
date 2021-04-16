from django.core.management.base import BaseCommand
from ._utils import (
    import_vocabulary,
    import_domain,
    import_concept_class,
    import_concept,
    import_concept_ancestor,
    import_relationship,
    import_concept_relationship,
    import_concept_synonym
)


# Default file names provided by Athena server
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

    help = "Imports all standardized vocabularies files obtained from the Athena server."

    def add_arguments(self, parser):
        parser.add_argument("--vocabulary", type=str, help="The vocabulary filename to import.")
        parser.add_argument("--domain", type=str, help="The domain filename to import.")
        parser.add_argument("--concept_class", type=str, help="The concept class filename to import.")
        parser.add_argument("--concept", type=str, help="The concept filename to import.")
        parser.add_argument("--concept_ancestor", type=str, help="The concept ancestor filename to import.")
        parser.add_argument("--relationship", type=str, help="The relationship filename to import.")
        parser.add_argument("--concept_relationship", type=str, help="The concept relationship filename to import.")
        parser.add_argument("--concept_synonym", type=str, help="The concept synonym filename to import.")

    def _import(self, value, function, required=True, **options):
        try:
            if options[value]:
                function(options[value])
            else:
                function(DEFAULT_FILENAMES[value])
            self.stdout.write(self.style.SUCCESS(f"Successfully imported {value}"))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"The {value.replace('_', ' ')} file is not found"))
            if required:
                exit()
            # if non-required files are not found the import continues
            else:
                pass

    def handle(self, *args, **options):
        values = ["vocabulary", "domain", "concept_class", "concept", "concept_ancestor",
                  "relationship", "concept_relationship", "concept_synonym"]
        functions = [import_vocabulary, import_domain, import_concept_class, import_concept, import_concept_ancestor,
                     import_relationship, import_concept_relationship, import_concept_synonym]
        required = [True, True, True, True, False, False, False, False]
        for value, function, required in zip(values, functions, required):
            self._import(value, function, required, **options)
