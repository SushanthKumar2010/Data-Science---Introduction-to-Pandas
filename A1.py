import pandas as pd
import numpy as np

exam_data = {'name': ['Anastasia','Dima','Katherine','James','Emily','Michael','Mathew','Laura','Kevin','Jonas'],
             'score' : [12.5, 9, np.nan,7,14,0,4.9,5.3,np.nan,7.1],
              'attempts' : [1,3,2,4,5,6,2,8,1,6],
              'qualify' : ['yes','no','no','yes','no','yes','yes','no','yes','no']}
labels = ['a','b','c','d','e','f','g','h','i','j']

df = pd.DataFrame(exam_data, index=labels)
print("Summary of the basic information about this dataframe and its data:")
print(df.info())