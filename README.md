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

### Null Values
- 5% of the dataset was randomly replaced with null values.
- This simulates missing real-world data.

### Outliers
- Some values in `first_semester_gpa` were set to **0**
- Some values in `admission_score` were set to **500**

These simulate abnormal or extreme cases.

## Purpose

The dataset is designed for classification tasks in Machine Learning, specifically predicting student dropout (Yes/No) in order to resolve the request made by the university to predict the chances of any student to dropout.
