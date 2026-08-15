from django.db import models
from django.conf import settings

from ocr.image_ocr.ocr_image import ProcessImage
from ocr.image_ocr.clean_ocr_output import ProcessOcr
from ocr.image_pre_processor.preprocess import PreProcessor
from bagsearch.models import VacuumBags


"""Push data through pipeline. Commit to database."""
def push_new_data():
    # 1. Preprocess the images in the raw directory
    image_processor = PreProcessor(settings.STORAGE_RAW_IMAGES_DIR, settings.STORAGE_PRE_PROCESSED_IMAGES_DIR)
    image_processor.preprocess()

    # 2. Recognises the text of all the, now pre-processed, images in the directory
    ocr_processor = ProcessImage(settings.STORAGE_PRE_PROCESSED_IMAGES_DIR)
        # Return -> list[dict[str, str]]:
    ocrtext = ocr_processor.scan_dir()

    # 3. Push data into model
    dictionaries = []
    for dictionary in ocrtext:
        result = VacuumBags(supermarket=dictionary["supermarket"], vacuum=dictionary["vacuum"], size=dictionary["size"])
        dictionaries.append(result)

    VacuumBags.objects.bulk_create(dictionaries)

