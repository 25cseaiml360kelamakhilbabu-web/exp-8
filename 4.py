#wap for statistical operations and broadcasting on arrays
import numpy as np

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print("Array A:", a)

# Statistical operations
print("Sum:", np.sum(a))
print("Mean:", np.mean(a))
print("Maximum:", np.max(a))
print("Minimum:", np.min(a))

# Broadcasting
print("A + 5:", a + 5)
print("A + B:", a + b)
