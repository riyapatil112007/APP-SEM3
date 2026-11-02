import numpy as np

# Create NumPy array using np.array()
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print("Array using np.array():")
print(arr1)

# Create NumPy array using np.arange()
arr2 = np.arange(1, 11)

print("\nArray using np.arange():")
print(arr2)

# Display array attributes
print("\nArray Attributes:")
print("Data Type:", arr1.dtype)
print("Shape:", arr1.shape)
print("Number of Dimensions:", arr1.ndim)
print("Size:", arr1.size)

# Indexing
print("\nFirst Element:", arr1[0])
print("Last Element:", arr1[-1])

# Slicing
print("Elements from index 2 to 5:", arr1[2:6])