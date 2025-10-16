#a. Write a Pandas program to create and display a one-dimensional array-like object containing an array of data using Pandas module.

import pandas as pd  
# Create a Pandas Series  
data = pd.Series([10, 20, 30, 40, 50])  
# Display the Series  
print("Pandas Series:")  
print(data)

# b. Write a Pandas program to convert a Panda module Series to Python list and its type.

import pandas as pd  
# Create a Pandas Series  
data = pd.Series([10, 20, 30, 40, 50])  
# Convert to Python list  
data_list = data.tolist()  
# Display the list and its type  
print("Python List:", data_list)  
print("Type:", type(data_list))

