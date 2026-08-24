# 🧹 Beutelnet: Matcht ihren Staubsauger mit dem kompatiblen Staubsaugerbeutel
Die größte Datenbank zu deutschen Staubsaugerbeuteln und den mit ihnen kompatiblen Staubsaugern. Beinhaltet die Eigenmarken von Edeka, Rewe und dm. Damit niemand mehr im Supermarkt stehen und ellenlange Verpackungsrückseiten durchlesen muss. Ein sehr wichtiges Projekt.

# Datensatz
Die Datenbank trackt mehr als 5.500 kompatible Produkte, verteilt auf drei Supermärkte.

| Anbieter | Beutelgrößen | Kompatible Produkte |
|----------|:---:|:---:|
| Edeka    | 4   | 1.095 |
| dm       | 11  | 1.952 |
| Rewe     | 7   | 2.527 |

# Datenquellen 
Die Daten stammen hauptsächlich aus zwei Quellen.
### 1. Verpackungen (OCR)
Einige Supermärkte, beispielsweise Edeka, haben ihre Verpackungsrückseiten nicht digitalisiert. Gelöst mit:
- Fotografieren der Verpackungsrückseiten
- Texterkennung mit Pythons Tesseract-Wrapper (OCR)
- Datenbereinigung mit Pandas

### 2. Websites (Scraping)
Andere Anbieter, etwa dm, stellen Daten online, allerdings verteilt über mehrere Seiten. Gelöst mit:
- Mehrere Selenium-Webscraper sammeln die Daten von den Websiten/Unterseiten
- Parsen zu einem einzelnen Datensatz
- Bereinigung von Ausreißern mit Pandas

# Die Django-App selbst aufsetzen
Um die Django-App `bagsearch` zu nutzen, benötigen Sie [Poetry](https://python-poetry.org/).

```bash
poetry install
```

Legen Sie die Daten anschließend im Verzeichnis `data/` in den entsprechenden Unterverzeichnissen ab.

Für Parsing von Verpackungsrückseiten, croppt man die Bilder so eng wie möglich. Die Logik zum Einspielen OCR-basierter Daten in ein Django-Model läuft dann über einen Django Custom Management Command:

```bash
poetry run manage.py push_new_data
```

Sie können die OCR-Daten auch erst einmal in eine Test-Datenbank oder eine CSV schreiben lassen:

```bash
# In ein Test-Model pushen
poetry run manage.py push_new_data --test

# Stattdessen als CSV exportieren
poetry run manage.py push_new_data --csv
```

## 🛠️ Stack

- **Backend:** Django
- **Frontend:** JavaScript and Bootstrap
- **Datenbank:** SQLite
- **OCR:** Tesseract (via Python-Wrapper)
- **Scraping:** Selenium
- **Datenverarbeitung:** Pandas
- **Dependency Management:** Poetry
