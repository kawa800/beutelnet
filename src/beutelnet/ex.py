import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'beutelnet.settings')
django.setup()

import csv
from bagsearch.models import VacuumBags

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'beutelnet.settings')
path = 'data/rewe/rewe-cleaned.csv'

with open(path) as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        VacuumBags.objects.get_or_create(
            supermarket = row[0],
            size = row[1],
            vacuum = row[2]
        )
