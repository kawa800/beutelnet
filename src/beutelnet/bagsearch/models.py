from django.db import models
from django.conf import settings

from ocr.image_ocr.ocr_image import ProcessImage
from ocr.image_ocr.clean_ocr_output import ProcessOcr
from ocr.image_pre_processor.preprocess import PreProcessor

# Create your models here.
class VacuumBags(models.Model):
    supermarket = models.CharField(max_length=200)
    vacuum = models.CharField(max_length=200)
    size = models.CharField(max_length=200)

    def __str__(self):
        return f"Supermarkt: {self.supermarket}, Staubsauger-Modell: {self.vacuum}, Beutelgröße: {self.size}"

    """ Return dict for JSON serialisation """
    def serialize(self):
        return {
            "supermarket": self.supermarket,
            "vacuum": self.vacuum,
            "size": self.size
        }
