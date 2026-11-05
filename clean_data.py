"""
Task 1: Data Cleaning and Preprocessing
Run: python clean_data.py
Requires: pandas
"""
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parent
input_file = ROOT / "raw_customer_data.csv"
output_file = ROOT / "cleaned_customer_data.csv"

df = pd.read_csv(input_file)
initial_rows = len(df)

# 1. Standardize column names: lowercase, trim, replace spaces with underscores.
df.columns = (
    df.columns.str.strip().str.lower()
    .str.replace(r"[^a-z0-9]+", "_", regex=True)
    .str.strip("_")
)

# 2. Trim whitespace in text columns.
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()

# 3. Remove exact duplicate rows.
before_duplicates = len(df)
df = df.drop_duplicates()
duplicates_removed = before_duplicates - len(df)

# 4. Standardize gender and country values.
gender_map = {
    "m": "Male", "male": "Male",
    "f": "Female", "female": "Female",
    "other": "Other", "non-binary": "Non-binary"
}
df["gender"] = df["gender"].str.lower().map(gender_map).fillna("Unknown")

country_map = {
    "india": "India",
    "usa": "United States",
    "united states": "United States",
    "pakistan": "Pakistan"
}
df["country"] = df["country"].str.lower().map(country_map).fillna("Unknown")

# 5. Convert numeric columns. Invalid strings become missing values.
df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["annual_income"] = pd.to_numeric(df["annual_income"], errors="coerce")

# Treat impossible ages as missing; keep plausible ages only.
df.loc[~df["age"].between(0, 100), "age"] = pd.NA

# Fill missing numeric values with the column median.
age_median = df["age"].median()
income_median = df["annual_income"].median()
df["age"] = df["age"].fillna(age_median).round().astype("int64")
df["annual_income"] = df["annual_income"].fillna(income_median).round().astype("int64")

# 6. Parse mixed date formats. Invalid dates become missing.
df["join_date"] = pd.to_datetime(df["join_date"], format="mixed", dayfirst=False, errors="coerce")
# Retain invalid/missing dates as blank rather than inventing a date.
df["join_date"] = df["join_date"].dt.strftime("%d-%m-%Y")

# 7. Standardize email text and fill missing email with an explicit label.
df["email"] = df["email"].str.lower().fillna("not_provided")

# 8. Save the cleaned data.
df.to_csv(output_file, index=False)

print(f"Rows at start: {initial_rows}")
print(f"Exact duplicates removed: {duplicates_removed}")
print(f"Rows after cleaning: {len(df)}")
print(f"Saved cleaned data to: {output_file.name}")
print("\\nRemaining missing values:")
print(df.isna().sum())
