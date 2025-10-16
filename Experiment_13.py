#a. Create and display a DataFrame from dictionary with index labels

import pandas as pd
 import numpy as np  
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily',
             'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no',
                'yes', 'yes', 'no', 'no', 'yes']
 }
 labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
 df = pd.DataFrame(exam_data, index=labels)
 print(df)

#b) Change the name 'James' to 'Suresh'

import pandas as pd
 import numpy as np  
exam_data = {
 'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily',
 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
 'qualify': ['yes', 'no', 'yes', 'no', 'no',
 'yes', 'yes', 'no', 'no', 'yes']
 }
 labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
 df = pd.DataFrame(exam_data, index = labels)
 df.loc[df['name'] == 'James', 'name'] = 'Suresh'
 print(df)


#c) Insert a new column into DataFrame
import pandas as pd
 import numpy as np  
exam_data = {
 'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily',
 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
 'qualify': ['yes', 'no', 'yes', 'no', 'no',
 'yes', 'yes', 'no', 'no', 'yes']
 }
 labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
 df = pd.DataFrame(exam_data, index = labels)
 df.loc[df['name'] == 'James', 'name'] = 'Suresh'
 df['age'] = [21, 23, 22, 25, 20, 24, 23, 21, 22, 26]
 print(df)

#d) Write a Pandas program to get list from DataFrame column headers.
import pandas as pd
 import numpy as np  
exam_data = {
 'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily',
 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
 'qualify': ['yes', 'no', 'yes', 'no', 'no',
 'yes', 'yes', 'no', 'no', 'yes']
 }
 labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
 df = pd.DataFrame(exam_data, index = labels)
 df.loc[df['name'] == 'James', 'name'] = 'Suresh'
 df['age'] = [21, 23, 22, 25, 20, 24, 23, 21, 22, 26]
 columns_list = list(df.columns)
 print( )
 print(columns_list)

#e) Write a Pandas program to get list from DataFrame column headers.
import pandas as pd
 import numpy as np 
exam_data = {
 'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily',
 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
 'qualify': ['yes', 'no', 'yes', 'no', 'no',
 'yes', 'yes', 'no', 'no', 'yes']
 }
 labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
 df = pd.DataFrame(exam_data, index = labels)
 df.loc[df['name'] == 'James', 'name'] = 'Suresh'
 df['age'] = [21, 23, 22, 25, 20, 24, 23, 21, 22, 26]
 columns_list = list(df.columns)
 print( )
 print(columns_list)
