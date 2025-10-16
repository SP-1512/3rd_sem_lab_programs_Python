#Write a NumPy program using NumPy methods - max, min, argmax, argmin, argmax, repr, count, bincount, unique.
 #a. To extract all numbers from a given array which are less and greater than a specified number.

import numpy as np
 # Create a sample NumPy array
 data = np.array([12, 5, 25, 7, 30, 18, 9, 45, 15])
 # Define the range to filter by
 min_val = 10
 max_val = 20
 print("Original array:", data)
 print(f"Filtering for numbers between {min_val} and {max_val}...")
 # Use boolean indexing to filter values in the specified range
 filtered_data = data[(data > min_val) & (data < max_val)]
 print("Extracted numbers:", filtered_data)


#b. To find the indices of the maximum and minimum numbers along the given axis of an array.

import numpy as np
 # Create a sample 2D NumPy array
 arr = np.array([[10, 20, 5],
 [15, 3, 25],
 [30, 8, 12]])
 print("Original array:")
 print(arr)
 # Find the indices of the maximum values along each row (axis=1)
 max_indices = np.argmax(arr, axis=1)
 # Find the indices of the minimum values along each row (axis=1)
 min_indices = np.argmin(arr, axis=1)
 print("\nIndices of the maximum values along each row:", max_indices)
 print("Indices of the minimum values along each row:", min_indices)
 # To verify, get the actual max and min values
 max_values = arr[np.arange(len(arr)), max_indices]
 min_values = arr[np.arange(len(arr)), min_indices]
 print("\nMaximum values:", max_values)
 print("Minimum values:", min_values)
