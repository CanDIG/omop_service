from django.core.management.base import BaseCommand
from ._utils import import_domains


class Command(BaseCommand):
    help = "Imports domain values from csv obtained from the Athena server."

    def add_arguments(self, parser):
        parser.add_argument("file", type=str, help="The filename to import.")

    def handle(self, *args, **options):
        file = options["file"]
        import_domains(file)
        self.stdout.write(self.style.SUCCESS('Successfully imported domains.'))
