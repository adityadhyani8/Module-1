import pandas as pd
import numpy as np

# 🔹 Step 1: Create sample dataset
data = {
    "Employee": ["Amit", "Neha", "Rahul", "Sneha", "Vikram", "Priya", "Arjun", "Divya"],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "Finance", "IT", "HR"],
    "Salary": [600000, 500000, np.nan, 700000, 520000, np.nan, 650000, 480000],
    "Temporary_Notes": ["On probation", "Contract", "Pending docs", "Verified",
                        "Intern", "New joiner", "On leave", "Temporary role"]
}

df = pd.DataFrame(data)
print("Initial DataFrame:\n", df)

# 🔹 Step 2: Detect missing values
print("\nMissing Values:\n", df.isnull().sum())

# 🔹 Step 3: Fill missing Salary values with mean
mean_salary = df["Salary"].mean(skipna=True)
df["Salary"] = df["Salary"].fillna(mean_salary)

# 🔹 Step 4: Drop Temporary_Notes column
df.drop(columns=["Temporary_Notes"], inplace=True)

# 🔹 Step 5: Rename Salary to Annual_Salary
df.rename(columns={"Salary": "Annual_Salary"}, inplace=True)

# 🔹 Step 6: Group by Department and compute mean salary & employee count
summary = df.groupby("Department").agg(
    Mean_Salary=("Annual_Salary", "mean"),
    Employee_Count=("Employee", "count")
).reset_index()

print("\nFinal Summary Table:\n", summary)