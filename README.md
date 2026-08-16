# 🧹 Beutelnet
Website to find the correct bag size for different vacuums.


# Dataset
Amount of data by (vacuum bag model, compatible products): 
* Edeka: (1,185)
* DM:  (11,1952)
* Rewe (7, 2500)



# Data
Data stems from two sources:
* OCR of packaging
    * Stores such as EDEKA haven't digitalised what vacuum cleaners the bag is compatible with at all. So I went into stores, took photos and gathered data from these images.
* Scraped data from groceries' websites
    * Rewe and DM have huge product lists. But the UI makes them difficult to search.

The custom command 'poetry run manage.py push_new_data' pushes OCR based data into the model.
The command fires up three modules in succession:
1. Apply pre-processing to the images.
2. Apply OCR
3. Push data into Django Model

The other dataset was data scraped with Selenium. Then cleaned with pandas. Again it was a one-time push into the dataset. As of now the pipeline is not automated, since the dataset is fixed.



