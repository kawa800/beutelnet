from django.db import models
from django.conf import settings

from ocr.image_ocr.ocr_image import ProcessImage
from ocr.image_ocr.clean_ocr_output import ProcessOcr
from ocr.image_pre_processor.preprocess import PreProcessor
from bagsearch.models import VacuumBags
from data.rewe import push_data


def _run_ocr_pipeline(model, raw_dir, preprocessed_dir):
    image_processor = PreProcessor(settings.raw_dir, settings.preprocessed_dir)
    image_processor.preprocess()

    # 2. Recognises the text of all the, now pre-processed, images in the directory
    ocr_processor = ProcessImage(settings.preprocessed_dir)
        # Return -> list[dict[str, str]]:
    ocrtext = ocr_processor.scan_dir()

    # 3. Push data into model
    dictionaries = []
    for dictionary in ocrtext:
        result = model(supermarket=dictionary["supermarket"], vacuum=dictionary["vacuum"], size=dictionary["size"])
        dictionaries.append(result)

    model.objects.bulk_create(dictionaries)


def push_new_OCR_data():
"""Push EDEKA data through pipeline. Commit to database."""
    _run_ocr_pipeline(
        VacuumBags,
        STORAGE_RAW_IMAGES_DIR,
        STORAGE_PRE_PROCESSED_IMAGES_DIR
    )

def test_push_OCR_data():
"""Push EDEKA data through pipeline. Commit to a testing database."""
    _run_ocr_pipeline(
        TestBags,
        STORAGE_RAW_IMAGES_DIR,
        STORAGE_PRE_PROCESSED_IMAGES_DIR
    )
