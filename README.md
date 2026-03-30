## Student Dropout Dataset - BRANDON VILLA
Related to the machine learning video made for Data Mining

## Description

This dataset simulates a university system to predict student dropout risk during the first academic year.

It contains demographic, academic, and financial data.

## Variables 

| Variable | Type | Range / Values | Description |
|----------|------|----------------|-------------|
|   age    | Numeric |    17–30    | Student age |
|  gender  | Categorical | Male, Female | Gender |
|  origin  | Categorical | Urban, Rural | Place of origin |
| highschool_gpa | Numeric | 2.0–5.0 | High school GPA |
| admission_score | Numeric | 200–400 | Admission test score |
| first_semester_gpa | Numeric | 1.5–5.0 | First semester GPA |
| socioeconomic_level | Numeric | 1–6 | Socioeconomic level |
| scholarship | Categorical | Yes, No | Scholarship status |
|   loan   | Categorical | Yes, No | Loan status |
|  dropout | Categorical | Yes, No | Target variable |

## Data Quality Simulation

## ⚠️ Data Quality Simulation

### Null Values
- Approximately 5% of the dataset was randomly selected and replaced with null (missing) values across different variables.
- The selection was performed independently for each column, meaning that missing values can appear in multiple attributes for the same record.
- This approach simulates real-world scenarios where data may be incomplete due to:
  - Errors during data collection
  - Missing survey responses
  - System or recording failures

Including null values is important because it allows testing data preprocessing techniques such as imputation, deletion, or handling missing data in Machine Learning pipelines.

### Outliers
- Artificial outliers were intentionally introduced in specific variables to simulate abnormal or extreme cases:
  - In `first_semester_gpa`, some values were set to **0**, which is outside the normal academic grading range (typically 1.5–5.0).
  - In `admission_score`, some values were set to **500**, exceeding the expected maximum score (200–400).

- These outliers represent potential real-world issues such as:
  - Data entry mistakes
  - Measurement errors
  - Exceptional or rare cases

Including outliers helps evaluate how robust Machine Learning models are when faced with noisy or extreme data, and allows the application of techniques such as outlier detection, normalization, or data cleaning.

## Purpose

The dataset is designed for classification tasks in Machine Learning, specifically predicting student dropout (Yes/No) in order to resolve the request made by the university to predict the chances of any student to dropout.
