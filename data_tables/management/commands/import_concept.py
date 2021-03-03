from django.core.management.base import BaseCommand
from ._utils import import_concept


class Command(BaseCommand):
    help = "Imports concepts from csv obtained from the Athena server."

    def add_arguments(self, parser):
        parser.add_argument("file", type=str, help="The filename to import.")

    def handle(self, *args, **options):
        import_concept(options["file"])
        self.stdout.write(self.style.SUCCESS("Successfully imported concepts."))
