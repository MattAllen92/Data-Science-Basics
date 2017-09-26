import pandas as pd

df = pd.read_csv(r"C:\Users\AllenM\Desktop\Projects\Basketball Data (SQL Python Test)\matt_allstar_cutdown.csv")

# missing data
print df.isnull() # show nulls T/F
print df.dropna() # drop whole rows with nulls
print df.fillna(int(df.mean())) # replace nulls with mean (int) NOTE: must use specific type depending on col type

import numpy as np
from sklearn.preprocessing import Imputer

df = pd.Series([1,2,3,np.NaN,5,6,None])

imp = Imputer(missing_values='NaN',    # could also use median, most_frequent
              strategy='mean', axis=0) # tell it to look for NaN and replace it with mean, look at cols (axis=1 would be rows)
imp.fit([1,2,3,4,5,6,7]) # give it the values it needs to fit
x = pd.Series(imp.transform(df).tolist()[0])
print x

http://www.dummies.com/programming/big-data/data-science/how-to-create-a-supervised-learning-model-with-logistic-regression/
more information in above link, try and figure out exactly how the imputer works and why you need to pass it the fit values

http://insidebigdata.com/2014/10/29/ask-data-scientist-handling-missing-data/