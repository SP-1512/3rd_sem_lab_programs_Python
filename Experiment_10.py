#Write a NumPy program using methods - info, add, array, all, greater, greater_equal, less, and less_equal, equal, allclose, zeros, ones, linspace, and  tolist.
 #a. To get help on the add function
import numpy as np
 # Get help on the numpy.add function
 help(np.add)
 # or in an interactive environment like Jupyter:
 # np.add?

 #b. To test whether none of the elements of a given array is zero.
import numpy as np
 # Create a sample array with no zeros
 arr1 = np.array([1, 2, 3, 4, 5])
 # Create a sample array with a zero
 arr2 = np.array([1, 0, 3, 4, 5])
 # Check if none of the elements are zero
 is_none_zero_1 = np.all(arr1 != 0)
 is_none_zero_2 = np.all(arr2 != 0)
 print("Array 1:", arr1)
 print("Are none of the elements zero?", is_none_zero_1)
 print("\nArray 2:", arr2)
 print("Are none of the elements zero?", is_none_zero_2)

 #c. To create an element-wise comparison (greater, greater_equal, less and less_equal, equal, equal within a tolerance) of two given arrays.
import numpy as np
 # Create two sample arrays
 arr1 = np.array([1, 2, 3, 4, 5])
 arr2 = np.array([1, 2, 3, 4, 5.000000001])
 print("Array 1:", arr1)
 print("Array 2:", arr2)
 # Element-wise comparisons
 print("\nGreater than:", arr1 > arr2)
 print("Greater than or equal to:", arr1 >= arr2)
 print("Less than:", arr1 < arr2)
 print("Less than or equal to:", arr1 <= arr2)
 print("Equal:", arr1 == arr2)
 # Equal within a tolerance
 tolerance_result = np.isclose(arr1, arr2, atol=1e-8)
 print("Equal within tolerance (atol=1e-8):", tolerance_result)
