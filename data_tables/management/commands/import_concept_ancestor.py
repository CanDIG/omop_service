from django.core.management.base import BaseCommand
from ._utils import import_concept_ancestor


class Command(BaseCommand):
    """ run: python manage.py import_concept_ancestor CONCEPT_ANCESTOR.csv """
    help = "Imports concept ancestor from csv obtained from the Athena server."

    def add_arguments(self, parser):
        parser.add_argument("file", type=str, help="The filename to import.")

    def handle(self, *args, **options):
        import_concept_ancestor(options["file"])
        self.stdout.write(self.style.SUCCESS("Successfully imported concept ancestors."))
