# Superstore CSV-to-SQL Data Cleaning & Ingestion Pipeline

An automated Python utility designed to standardize raw transactional CSV exports, handle missing data, and load sanitized schemas directly into a database environment.

## Pipeline Steps
1. **Data Ingestion:** Reads raw `superstore.csv` files using Pandas.
2. **Data Cleaning:** Drops null/missing records and programmatically normalizes column headers into standard lowercase `snake_case` naming conventions.
3. **Database Loading:** Connects to an SQLite database (`pipeline.db`) and overwrites the target `clean_orders` table with clean, analysis-ready data.

## Tech Stack
* **Language:** Python
* **Libraries:** Pandas, SQLite3
* **Database:** SQLite
