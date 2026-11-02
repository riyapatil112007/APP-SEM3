import pandas as pd
import numpy as np

# Generate 10 random numbers
random_numbers = np.random.randint(1, 100, 10)

# Create Pandas Series with default index
s1 = pd.Series(random_numbers)

print("Pandas Series with Default Index:")
print(s1)

# Create Series with custom index
s2 = pd.Series(random_numbers, index=[
    'a', 'b', 'c', 'd', 'e',
    'f', 'g', 'h', 'i', 'j'
])

print("\nPandas Series with Custom Index:")
print(s2)

# Display Series attributes
print("\nSeries Attributes:")
print("Data Type:", s1.dtype)
print("Shape:", s1.shape)
print("Size:", s1.size)
print("Index:", s1.index)

# Statistical operations
print("\nMean:", s1.mean())
print("Maximum:", s1.max())
print("Minimum:", s1.min())
print("Sum:", s1.sum())

# Sorting
print("\nSorted Series:")
print(s1.sort_values())

# Filtering
print("\nNumbers greater than 50:")
print(s1[s1 > 50])