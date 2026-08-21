import csv

from django.db import models
from django.conf import settings

from ocr.image_ocr.ocr_image import ProcessImage
from ocr.image_ocr.clean_ocr_output import ProcessOcr
from ocr.image_pre_processor.preprocess import PreProcessor

from bagsearch.models import VacuumBags
from bagsearch.models import TestBags 


def _run_ocr_pipeline(model, raw_dir, preprocessed_dir):
    image_processor = PreProcessor(raw_dir, preprocessed_dir)

    # 2. Recognises the text of all the, now pre-processed, images in the directory
    ocr_processor = ProcessImage(preprocessed_dir)
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
        settings.STORAGE_RAW_IMAGES_DIR,
        settings.STORAGE_PRE_PROCESSED_IMAGES_DIR
    )

def test_push_OCR_data():
    """Push EDEKA data through pipeline. Commit to a testing database."""
    _run_ocr_pipeline(
        TestBags,
        settings.STORAGE_RAW_IMAGES_DIR,
        settings.STORAGE_PRE_PROCESSED_IMAGES_DIR
    )


""" Create CSV from currently loaded images """
def create_csv() -> None:
    pre_processor = PreProcessor(settings.STORAGE_RAW_IMAGES_DIR, settings.STORAGE_PRE_PROCESSED_IMAGES_DIR)
    pre_processor.preprocess()
    ocr_processor = ProcessImage(settings.STORAGE_PRE_PROCESSED_IMAGES_DIR)
    ocr_output = ocr_processor.scan_dir()
    print(ocr_output)

    if not ocr_output:
        print("No OCR output")
        return

    try:
        with open("data/edeka/data.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=ocr_output[0].keys())
            writer.writeheader()
            writer.writerows(ocr_output)

    except Exception as e:
        print(f"Error writing CSV{e}")
