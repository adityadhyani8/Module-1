import pandas as pd

# 1. Ask user how many records they want to enter
n = int(input("Enter number of records: "))

# 2. Collect dataset details from user
records = []
for i in range(n):
    print(f"\n--- Record {i+1} ---")
    name = input("Enter Name: ")
    score = float(input("Enter Score: "))
    category = input("Enter Category (e.g., A, B): ")

    # Automatically set Passed based on score
    passed = score > 85

    records.append({"Name": name, "Score": score, "Passed": passed, "Category": category})

# 3. Create DataFrame
df = pd.DataFrame(records)

# 4. Filter high-performing students (Score > 85)
high_performers = df[df["Score"] > 85][["Name", "Score"]].sort_values(by="Score", ascending=False)

# 5. Show only Name and Score of high performers
print("\n--- High-Performing Students (Score > 85) ---")
print(high_performers)