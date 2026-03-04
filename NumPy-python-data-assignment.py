import numpy as np

# 1. Ask user for dataset dimensions
num_samples = int(input("Enter number of samples (rows): "))
num_features = int(input("Enter number of features (columns): "))

# 2. Set random seed for reproducibility
np.random.seed(42)

# 3. Generate dataset with user-defined shape
data = np.random.randn(num_samples, num_features)

# 4. Compute mean and std per feature
mean = data.mean(axis=0)
std = data.std(axis=0)

# 5. Normalize using broadcasting
normalized = (data - mean) / std

# 6. Slice into training (first 80%) and test (last 20%)
train_size = int(0.8 * normalized.shape[0])
training_data = normalized[:train_size]
test_data = normalized[train_size:]

# 7. Demonstrate view behavior
print("Before modification:", training_data[0, 0])
training_data[0, 0] = 999  # Intentional modification
print("After modification:", normalized[0, 0])  # Shows effect on original

# 8. Print shapes and explanation
print("\n--- Pipeline Summary ---")
print("Original data shape:", data.shape)
print("Mean shape:", mean.shape)
print("Standard deviation shape:", std.shape)
print("Training data shape:", training_data.shape)
print("Test data shape:", test_data.shape)
print("Note: Modifying the training slice affected the original normalized array (views share memory).")