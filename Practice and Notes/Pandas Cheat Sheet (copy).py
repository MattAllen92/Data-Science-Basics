##Pandas##

##############################################################################

##Modules

#libraries
import pandas as pd
import numpy as np
from sklearn import datasets

#library info
pd.__version__
pd.show_versions()

##############################################################################

##Input Data

#dictionary
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
        
#array
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


##############################################################################

##Data Frames

#create df
df = pd.DataFrame(data, index=labels)

#show df info
df.info()
df.describe()

##############################################################################

#Filter Data Frames

#show top 3 rows
df.iloc[:3]
df.head(3)
#show animal and age cols
df[['animal', 'age']]
#show animal and age cols, rows a to c
df.loc['a':'c', ['animal', 'age']]
#show animal and age cols, rows 4, 5 and 9
df.ix[[3, 4, 8], ['animal', 'age']]
#show rows where visits > 3
df[df['visits'] >= 3]
#show rows where age is null/empty
df[df['age'].isnull()]
#show cats younger than 3
df[(df['animal'] == 'cat') & (df['age'] < 3)]
#show animals between 2 and 4
df[df['age'].between(2, 4)]

##############################################################################

#Editing Data Frames
#set row f age to 1.5
df.loc['f', 'age'] = 1.5
#add row to df
df.loc['k'] = [5.5, 'dog', 'no', 2]
#remove row from df
df = df.drop('k')
#sort df by age (desc) then visits (asc)
df.sort_values(by=['age', 'visits'], ascending=[False, True])
#replace yes and no with True and False in priority col
df['priority'] = df['priority'].map({'yes': True, 'no': False})
#replace snake with python in animal col
df['animal'] = df['animal'].replace('snake', 'python')

##############################################################################

#Calculating with Data Frames

#sum all visits
df['visits'].sum()
#show mean age for each animal
df.groupby('animal')['age'].mean()
#sum counts for each animal
df['animal'].value_counts()

##############################################################################

#Plotting data# line graphs
dataset.plot() # simple plot of one variable on top of the other
dataset.plot(kind='box') # side by side box plot (b/c scales are ~ the same)
dataset.cumsum().plot() # plot cumulative sum of dataset values

# other plot types (there are more but they require more inputs etc.)
dataset.plot.box()
dataset.plot.bar() # or barh for horizontal
dataset.plot.density()
dataset.plot.hist()
dataset.plot.line()
dataset.plot.kde()

# plots with parameters
dataset.plot.bar(stacked=True)
dataset.plot.hist(alpha=0.5)