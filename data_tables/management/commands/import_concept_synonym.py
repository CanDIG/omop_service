from django.core.management.base import BaseCommand
from ._utils import import_concept_synonym


class Command(BaseCommand):
    """ run: python manage.py import_concept_synonym CONCEPT_SYNONYM.csv """
    help = "Imports concept synonyms from csv obtained from the Athena server."

    def add_arguments(self, parser):
        parser.add_argument("file", type=str, help="The filename to import.")

    def handle(self, *args, **options):
        import_concept_synonym(options["file"])
        self.stdout.write(self.style.SUCCESS("Successfully imported concept synonyms."))
