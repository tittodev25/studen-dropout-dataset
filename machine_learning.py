# Made by Brandon Villa

import pandas as pd
import numpy as np

# With this we set a random seed to ensure reproducibility
# This means every time the code runs, it generates the same dataset
np.random.seed(42)

# The number of records requested:
n = 500

# Here we create the base dataset with different types of variables

data = pd.DataFrame({
    # Demographic Data
    "age": np.random.randint(17, 30, n),
    "gender": np.random.choice(["Male", "Female"], n),
    "origin": np.random.choice(["Urban", "Rural"], n),

    # Academic Data
    "highschool_gpa": np.round(np.random.uniform(2.0, 5.0, n), 2),
    "admission_score": np.random.randint(200, 400, n),
    "first_semester_gpa": np.round(np.random.uniform(1.5, 5.0, n), 2),

    # Financial Data
    "socioeconomic_level": np.random.choice([1, 2, 3, 4, 5, 6], n),
    "scholarship": np.random.choice(["Yes", "No"], n),
    "loan": np.random.choice(["Yes", "No"], n)
})

# Here we create the target variable (dropout)
# Then the logic -> Students are more likely to drop out if:
# - Their first semester GPA is low (< 3.0)
# - OR their admission score is low (< 250)

data["dropout"] = np.where(
    (data["first_semester_gpa"] < 3.0) |
    (data["admission_score"] < 250),
    "Yes", "No"
)


# Now then we introduce missing values (nulls)
# For each column, randomly select 5% of the rows and assign NaN
# This simulates incomplete or missing real-world data

for col in data.columns:
    data.loc[data.sample(frac=0.05).index, col] = np.nan

# Introduce outliers (extreme or abnormal values)
# 2% of the data will be modified to simulate errors or unusual cases

data.loc[data.sample(frac=0.02).index, "first_semester_gpa"] = 0
data.loc[data.sample(frac=0.02).index, "admission_score"] = 500

# This just save the files with the dataset
data.to_csv("student_dropout_dataset.csv", index=False)

print("Dataset created!")