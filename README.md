# Task 1: Data Cleaning and Preprocessing

## Objective
Clean a raw customer dataset containing missing values, duplicate rows, inconsistent text, mixed date formats, and incorrect data types.

## Files
- `raw_customer_data.csv` — sample raw dataset containing intentional data-quality issues.
- `cleaned_customer_data.csv` — cleaned output generated from the raw dataset.
- `clean_data.py` — Python Pandas script used for cleaning.
- `cleaning_summary.md` — summary of changes and decisions.
- `interview_questions.md` — short answers to the assignment interview questions.

## Requirements
- Python 3.9+
- pandas

Install pandas:
```bash
pip install pandas
```

## Run the project
Keep all files in the same folder, open a terminal in this folder, and run:
```bash
python clean_data.py
```
The script reads `raw_customer_data.csv` and creates/overwrites `cleaned_customer_data.csv`.

## Cleaning steps
1. Standardize column names.
2. Trim whitespace from text.
3. Remove exact duplicate rows.
4. Standardize gender and country categories.
5. Convert age and income to numeric values.
6. Treat impossible ages as missing and impute missing numeric values with medians.
7. Parse dates and format valid dates as `dd-mm-yyyy`.
8. Normalize email case and mark missing email values.
9. Export the cleaned CSV.

## Dataset note
The included dataset is synthetic and designed for learning. It is not personal or real customer data.
