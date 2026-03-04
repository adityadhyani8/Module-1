import pandas as pd

# 1. Create a small sample dataset
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ian", "Jane"],
    "Age": [25, 30, 35, 40, 22, 28, 33, 45, 29, 31],
    "Score": [88, 76, 90, 65, 70, 85, 92, 55, 80, 78],
    "Label": ["A", "B", "A", "C", "B", "A", "A", "C", "B", "A"]
}

# Save dataset to CSV
csv_filename = "sample_dataset.csv"
pd.DataFrame(data).to_csv(csv_filename, index=False)

# 2. Load dataset using pd.read_csv()
df = pd.read_csv(csv_filename)

# 3. Display first 5 rows
print("\n--- First 5 rows ---")
print(df.head())

# 4. Display last 5 rows
print("\n--- Last 5 rows ---")
print(df.tail())

# 5. Structural information
print("\n--- Dataset Info ---")
print(df.info())

# 6. Summary statistics
print("\n--- Summary Statistics ---")
print(df.describe())

# 7. Select a single column
ages = df["Age"]
print("\n--- Single Column (Age) ---")
print(ages)

# 8. Select multiple columns
subset = df[["Name", "Score"]]
print("\n--- Multiple Columns (Name & Score) ---")
print(subset)

# 9. Filter rows based on condition (Score > 80)
filtered = df[df["Score"] > 80]
print("\n--- Filtered Rows (Score > 80) ---")
print(filtered)