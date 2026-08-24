# 🧹 Beutelnet: Match ihren Staubsauger mit dem kompatiblen Staubsaugerbeutel
Die größte Datenbank zu deutschen Staubsaugerbeuteln und den mit ihnen kompatiblen Staubsaugern. Beinhaltet die Eigenmarken von Edeka, Rewe und DM. Damit man nicht im Supermarkt stehen muss, und ellenlange Verpackungsrückseiten durchlesen muss - eine höchstwichtigste Anwendung.

# Datensatz
Die Datenbank trackt mehr als 5.500 kompatible Produkte. Die Anzahl der Staubsaugerbeutel-Größen zu kompatiblen Produkten sind:
* Edeka: (4,1095)
* DM:  (11,1952)
* Rewe (7, 2527)

# Datenquellen 
Die Daten stammen hauptsächlich aus zwei Quellen.
* Verpackungen
    * Supermärkte wie EDEKA haben ihre Verpackungsrückseiten nicht digitalisiert. Die Rückseiten wurden fotografiert und der Text wurde dann mit Python's Tesseract Wrapper (OCR) prozessiert. Mit Python-Skripten und Pandas wurden die Daten dann bereinigt.
* Websiten
    * Supermärkte wie DM haben mehrere Daten dazu, welcher Staubsauger zu welchem Staubsaugerbeutel passt. Diese sind jedoch über mehrere Websiten verstreut. Mehrere Selenium-Webscraper haben diese Websiten durchscraped und zu einem einzelnen Datensatz zusammengefasst. Auch hier wurden Ausreißer mit Pandas bereinigt.

# Bedienung
Falls Sie die Django-App 'bagsearch' importieren möchten, benötigen Sie poetry. Daraufhin legen Sie ihre Daten im Verzeichnis 'data' und den entsprechenden Verzeichnissen ab.
Die Hauptlogik, um OCR-basierte Daten in ein Django-Model zu pushen funktioniert über den Django-Custom-Command:
`poetry run manage.py push_new_data`. Croppen Sie dabei die Bilder der Verpackungsrückseiten so eng wie möglich. Die Logik in der Directory 'ocr' wendet daraufhin Preprocessing, wie etwa Grayscaling, an und pusht die Daten in eine SQLite Datenbank.
Mit folgenden Optionen können Sie die Daten auch erst einmal in ein Test-Model oder eine CSV pushen:
`poetry run manage.py push_new_data --test`
`poetry run manage.py push_new_data --csv`
