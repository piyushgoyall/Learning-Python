import pandas as pd
data = {'Calories': [300, 200, 100], 'Duration':[30,20,10]}

myDataFrame = pd.DataFrame(data)
print(myDataFrame)

listA = ['Red', 'Blue', 'Yellow', 'Pink', 'Orange']
S1 = pd.Series(listA)
print(S1)
print()

S1[0]
S1[1]

myDataFrame.loc[0]

series2=pd.Series(['kavi','shyam','ravi'],index=[3,5,1])
print(series2)
print()

import numpy as np # import NumPy with alias np
import pandas as pd
array1 = np.array([1,2,3,4])
series3 = pd.Series(array1)
print(series3)
print()

series3 = pd.Series(array1, index = ["Jan","Feb", "Mar", "Apr"])

dict1 = {'India': 'NewDelhi', 'UK':
'London', 'Japan': 'Tokyo'}
print(dict1) #Display the dictionary
{'India': 'NewDelhi', 'UK': 'London', 'Japan':
'Tokyo'}
series8 = pd.Series(dict1)
print(series8)



# import pandas as pdf


# list1 = ["green","pink","black","yellow","purple","white","cyan","olive"]
# xyz = pdf.Series(list1)
# print(xyz)
# print(list1[0])
# print(list1[1])
# print(list1[2])
# print(list1[3])


# # data = {
# #     "Calories": [300, 200, 400],
# #     "Duration": [30, 20, 90]
# # }

# # MyDataFrame = pdf.DataFrame(data)
# # print(MyDataFrame)
