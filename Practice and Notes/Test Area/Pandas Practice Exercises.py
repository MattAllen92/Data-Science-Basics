#Medium Pandas Exercises

#modules
import pandas as pd
import numpy as np

#1)
#create df
df = pd.DataFrame({'A':[1,2,2,3,4,5,5,5,6,7,7]})
#filter out rows containing same int as previous row
df.loc[df['A'].shift() != df['A']] #shift moves rows on by one, therefore you're checking if the next row equals the current row

#2)
#create df
df = pd.DataFrame(np.random.random(size=(5,3)))
#subtract row mean from each value
df.sub(df.mean(axis=1), axis=0)

#3)
df = pd.DataFrame(np.random.random(size=(10, 10)), index=list('abcdefghij'))
#a)
#find column with smallest sum
df.sum().idxmin() #first occurence of min value within range, ignores null values

#b)
#count unique rows within a dataframe (ignoring duplicate rows)
len(df) - df.duplicated(keep=False).sum() #the second part calculates the sum of duplicated rows
#or...
len(df.drop_duplicates(keep=False))