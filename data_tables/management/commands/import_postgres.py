from django.core.management.base import BaseCommand
from ._utils import import_postgres


class Command(BaseCommand):
    """ run: python manage.py import_postgres """
    help = "Imports Standardized vocabularies from csv obtained from the Athena server."

    def handle(self, *args, **options):
        import_postgres()
        self.stdout.write(self.style.SUCCESS("Successfully imported all Standardized vocabularies."))
