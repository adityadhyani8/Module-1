import numpy as np

# 1. Ask user to enter numeric values separated by spaces
user_input = input("Enter numeric values separated by spaces: ")

# 2. Convert input string into a NumPy array of floats
data = np.array(user_input.split(), dtype=float)

# 3. Compute mean and standard deviation
mean = data.mean()
std = data.std()

# 4. Normalize the data
normalized = (data - mean) / std

# 5. Reshape normalized data into a 2D array
# Example: reshape into 2 rows (adjust as needed)
rows = int(input("Enter number of rows for reshaping: "))
reshaped = normalized.reshape(rows, -1)

# 6. Print results
print("\n--- Preprocessing Pipeline ---")
print("Original data:", data)
print("Mean:", mean)
print("Standard Deviation:", round(std, 2))
print("Normalized data:", normalized)
print("Reshaped data:\n", reshaped)
print("Reshaped data shape:", reshaped.shape)