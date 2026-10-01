#wap for saving and loading arrays
import numpy as np

# Create an array
a = np.array([10, 20, 30, 40, 50])

# Save the array
np.save("data.npy", a)
print("Array saved")

# Load the array
b = np.load("data.npy")
print("Array loaded:", b)
 
