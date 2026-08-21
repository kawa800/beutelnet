from django.core.management.base import BaseCommand, CommandError
from bagsearch.models import VacuumBags

from bagsearch.pushdata import push_new_OCR_data 
from bagsearch.pushdata import test_push_OCR_data 
from bagsearch.pushdata import create_csv 

class Command(BaseCommand):
    help="Pushing newly processed image text into database."

    def add_arguments(self, parser):
        parser.add_argument("--test",
                            action="store_true",
                            help="push data into test database bagsearch_testbags"
                            )

        parser.add_argument("--csv",
                            action="store_true",
                            help="push data into csv"
                            )


    def handle(self, *args, **kwargs):
        if kwargs["test"]:
            test_push_OCR_data()
        elif kwargs["csv"]:
            create_csv()
        else:
            push_new_OCR_data()
            print("Inserted new data.")
