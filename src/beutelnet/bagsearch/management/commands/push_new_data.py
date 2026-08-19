from django.core.management.base import BaseCommand, CommandError
from bagsearch.models import VacuumBags

from bagsearch.pushdata import pushdata

class Command(BaseCommand):
    help="Pushing newly processed image text into database."

    def handle(self, *args, **kwargs):
        push_new_OCR_data()
        print("Inserted new data.")
