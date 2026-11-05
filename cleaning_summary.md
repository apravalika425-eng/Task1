# Cleaning Summary

- Input file: `raw_customer_data.csv`
- Output file: `cleaned_customer_data.csv`
- Rows in raw dataset: 12
- Rows after removing exact duplicate records: 11
- Exact duplicate rows removed: 1
- Column headers converted to lowercase snake_case.
- Leading/trailing spaces removed from text values.
- Gender values standardized to Male, Female, Other, and Non-binary.
- Country values standardized (USA and United States mapped to United States).
- Age and annual_income converted to numeric values; invalid entries converted to missing values.
- Implausible ages outside 0–100 treated as missing.
- Missing/invalid age and annual_income values filled using each column's median.
- Mixed date formats parsed and output as dd-mm-yyyy; invalid dates left blank.
- Email values converted to lowercase; missing email marked as `not_provided`.

## Important note
This is a small illustrative customer dataset created for this assignment. Median imputation is a simple demonstration choice; in a real project, choose missing-value treatment based on business context and document the decision. The date `31/06/2024` is invalid and is therefore left blank rather than guessed.
