import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Practice for Aiaoon
x = 5 + 6 + 7 + 10 + 20 + 2 + 3 + 4 + 20
print(x)

print(str('Aiaoon') + '-' + str('GrandMother') + '-' + 'Grand father' + '-' +'Uncle Ow' + '-' + 'A' + '&' + 'Tou')

# name = ['Aiaoon', 'Mama', 'Papa', 'Ow-uncle', 'Grand Mother of Mama', 'Grand Father of Mama','Grand Mother of Papa', 'Grand Father of Papa' ]

name = ['Aiaoon', 'Mama', 'Papa', 'Ow-uncle', 'ยาย', 'ตา', 'ปู่', 'ย่า']

age = [4, 39, 40, 43, 67, 69, 60, 58]

# df = pd.DataFrame(data=[[name, age]], columns=['name', 'age'])
ds = pd.DataFrame({'name': name, 'age': age})

# print(df.head())
print(ds)

## Change to font 'Tomaho' for 'thai'
# print(plt.rcParams)
# print(plt.rcParams['font.family']) # original font
# print(plt.rcParams)
plt.rcParams['font.family'] = 'Tomaho'
plt.bar(x=name, height=age,data=ds)
plt.show()
