# libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn as skl
from sklearn.model_selection import cross_val_predict

# load data
raw_data = r"C:\Users\AllenM\Desktop\Projects\Python Machine Learning Exercises\data\ex1data1.txt"
col_names = ["Population", "Profit"]
dataset = pd.read_csv(raw_data, names = col_names)

# examine data
dataset.describe()
dataset.head(20)
dataset.shape

# visualize data

# extract and scatter plot data
array = dataset.values # extract dataset values into multi-array
x_val = array[:,0] # extract population for x
y_val = array[:,1] # extract profit for y
plt.scatter(x_val, y_val, marker='x', c='r') # marker is how the points appear, c is colour
plt.title('Distribution of Profits')
plt.xlabel('Population (M)')
plt.ylabel('Profit (M)')
plt.show()

# or simply: dataset.plot(kind='scatter', x='Population', y='Profit', figsize=(12,8))

# this graph shows us that there is a ~ linear relationship between the population
# and the profit. Because we are trying to determine the relationship between
# one independent and one dependent variable (and no classify anything), here
# we want to use a simple (i.e. not multiple) linear regression.

lr = skl.linear_model.LinearRegression() # create linear regression package
predicted = cross_val_predict(lr, dataset.values, y_val, cv=10) # predict values based on inputs via cross-validation
fig, ax = plt.subplots() # no clue
ax.scatter(y_val, predicted) # scatter plot of input vs. predicted
ax.plot([y_val.min(), y_val.max()], [y_val.min(), y_val.max()], 'k--', lw=4) # set axis scale
ax.set_xlabel('Measured') # label x
ax.set_ylabel('Predicted') # label y
plt.show() # show