# Import the required libraries
import numpy as np
import matplotlib.pyplot as plt

# Create the epochs list (1 to 10)
epochs = list(range(1, 11))

# Generate synthetic training loss values using NumPy
# Example: exponential decay with some noise
loss = np.exp(-0.3 * np.array(epochs)) + np.random.normal(0, 0.02, len(epochs))

# ---------------- Line Plot ----------------
plt.figure(figsize=(8, 5))
plt.plot(epochs, loss, marker='o', linestyle='-', color='blue', label='Training Loss')
plt.title("Loss vs Epoch")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.grid(True)
plt.legend()
plt.show()

# ---------------- Scatter Plot ----------------
plt.figure(figsize=(8, 5))
plt.scatter(epochs, loss, color='red', marker='x')
plt.title("Epoch vs Loss (Scatter Plot)")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.grid(True)
plt.show()

# ---------------- Bar Chart ----------------
models = ["Model A", "Model B", "Model C"]
accuracy = [0.85, 0.90, 0.88]

plt.figure(figsize=(8, 5))
plt.bar(models, accuracy, color=["green", "blue", "orange"])
plt.title("Model Accuracy Comparison")
plt.xlabel("Models")
plt.ylabel("Accuracy")
plt.ylim(0.8, 1.0)  # zoom in for better view
plt.show()