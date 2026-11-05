Task 1: Data Cleaning and Preprocessing

Data Analyst Internship

1. Objective

The main objective of this task is to clean and prepare a raw dataset by identifying and handling missing values, duplicate records, inconsistent formats, and incorrect data types.

2. Tools Used

- Python
- Pandas Library
- CSV Dataset
- GitHub

3. Dataset

Customer Data containing the following columns:

- Customer ID
- Name
- Age
- Gender
- Country
- Signup Date
- Purchase Amount
- Email

4. Data Cleaning Steps

1. Handling Missing Values: Identified missing values and filled numeric missing values using median values.
2. Removing Duplicates: Removed duplicate records using "drop_duplicates()".
3. Standardizing Text: Standardized gender and country names.
4. Date Formatting: Converted different date formats into a consistent format (YYYY-MM-DD).
5. Column Names: Renamed column headers into lowercase with underscores.
6. Data Types: Converted age and purchase amount into numeric data types.
7. Invalid Values: Identified invalid ages and date values.

5. Python Libraries

import pandas as pd

6. Output

The cleaned dataset is saved as:

"cleaned_customers.csv"

A cleaning summary is also generated to explain the changes made to the dataset.

7. Project Structure

data-cleaning-task1/
│
├── data/
│   └── raw_customers.csv
│
├── outputs/
│   ├── cleaned_customers.csv
│   └── cleaning_summary.txt
│
├── src/
│   └── clean_data.py
│
├── requirements.txt
├── .gitignore
└── README.md

8. Conclusion

This task helped me understand the importance of data cleaning and preprocessing. I learned how to handle missing values, remove duplicate records, standardize data, and prepare a clean dataset using Python and Pandas.

Internship Task: Data Analyst Internship
Task Number: Task 1
Project: Data Cleaning and Preprocessing# Task1