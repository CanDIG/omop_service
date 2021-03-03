from django.core.management.base import BaseCommand
from ._utils import import_concepts


class Command(BaseCommand):
    help = "Imports vocabularies values from csv obtained from the Athena server."

    def add_arguments(self, parser):
        parser.add_argument("file", type=str, help="The filename to import.")

    def handle(self, *args, **options):
        file = options["file"]
        import_concepts(file)
        self.stdout.write(self.style.SUCCESS('Successfully imported vocabularies.'))
