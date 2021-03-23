from django.core.management.base import BaseCommand
from ._utils import import_relationship


class Command(BaseCommand):
    """ run: python manage.py import_relationship RELATIONSHIP.csv """
    help = "Imports relationships from csv obtained from the Athena server."

    def add_arguments(self, parser):
        parser.add_argument("file", type=str, help="The filename to import.")

    def handle(self, *args, **options):
        import_relationship(options["file"])
        self.stdout.write(self.style.SUCCESS("Successfully imported relationships."))
