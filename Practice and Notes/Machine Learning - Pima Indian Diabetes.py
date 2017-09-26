# libraries
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.tools.plotting import scatter_matrix

############################################################################

# 1) LOAD DATA

# common data loading code
in_data_file = r'C:\Users\AllenM\Desktop\TGI-Ops\MA Programs\Python Scripts\Practice and Notes\Data Sets\Pima Indian Diabetes.csv'
raw_data = open(in_data_file, 'rt') # open file to read as text

# a) standard python libs (into numpy array)
#reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE) # read text as csv, removing quotes
#x = list(reader) # convert to list of lines
#data = np.array(x).astype('float') # convert to numpy array

# b) numpy (into numpy array)
#data = np.loadtxt(raw_data, delimiter=',') # load file data into numpy array

# c) pandas (into pandas data frame)
col_names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
features = col_names[:-1]
class_label = col_names[-1]
data = pd.read_csv(in_data_file, names=col_names)

############################################################################

# 2) ANALYSE/INSPECT DATA

# examine the data (could do anything relating to series e.g. plot them against each other)
data.head(20) # view top 20 rows
print(data.shape) # print (rowNum, colNum) -> if data is too big it will take ages to train
                                                       # too small and it won't be useful
pd.Series.value_counts(data['class']) # classes/labels contain 0s or 1s (500:268)
plt.show(scatter_matrix(data[features])) # show scatter plot of data features        
print(data.dtypes) # show data types (e.g. int64)
pd.set_option('display.width', 100) # set col widths for describe() below
pd.set_option('precision', 3) # set 3 dp for describe() below
print(data.describe()) # show count, mean, std, min, percentiles, max
print(data.corr(method='pearson')) # show correlation between vars (-1 = inverse, 1 = positive, 0 = no correlation)
                                   # some ML algorightms aren't good if vars are highly correlated
                                   # Pearson method assumed normal distribution of variables
print(data.skew()) # many ML algorithms assume a Guassian (normal) distribution, if data is skewed to L or R then it
                   # needs to be shifted back towards the middle before use. Skew shows how much data is skewed to the
                   # left (-ve) or right (+ve)
                   
# more info on plotting and visualisation here:
# http://machinelearningmastery.com/visualize-machine-learning-data-python-pandas/

# Data Info:
# 768 rows and 9 cols
# All patients are females over 21 years of age
# No actual missing values but some have been set to 0
# Cols: 
# 1. Number of times pregnant 
# 2. Plasma glucose concentration at 2 hours in an oral glucose tolerance test 
# 3. Diastolic blood pressure (mm Hg) 
# 4. Triceps skin fold thickness (mm) 
# 5. 2-Hour serum insulin (mu U/ml) 
# 6. Body mass index (weight in kg/(height in m)^2) 
# 7. Diabetes pedigree function 
# 8. Age (years) 
# 9. Class variable (0 or 1)

############################################################################

# PREPARE THE DATA/PRE-PROCESSING

# ML algorithms make assumptions about your data depending which one you pick, therefore make sure the data you use
# has been made to fit the assumptions of the ML algorithm you select

# with ML the key is to expose the data structure to the algorithm in the way that suits it best. Sometimes this
# requires a tonne of pre-processing, others this requires none. A good method to use is to create a few different
# sets of data, each with different structures and see which produces the best results with the algorithm

# a) Re-scaling (~Normalising) Data (sklearn MinMaxScaler)
# If features in a data set have wildly varying scales then ML algorithms can struggle to make sense of them, scaling
# the data overcomes this and is particularly useful for optimisation (gradient descent), weighting methods
# (regression, neural networks) and distance measures (K-nearest neighbour)

import scipy
from sklearn.preprocessing import MinMaxScaler

array = data.values # create array (gets rid of issue with types e.g. 'could not convert preg from string to float')
features = array[:,0:8] # extracts features (all rows, cols 0-7)
labels = array[:,8] # extract labels (all rows, col 8)
scaler = MinMaxScaler(feature_range=(0,1)) # create scaler between 0 and 1
rescaled_features = scaler.fit_transform(features) # apply scaler to features
print(rescaled_features[0:5,:]) # show first 5 rows, all cols -> values are between 0 and 1

# b) Standardising Data (sklearn StandardScaler)
# This method transforms attributes with Gaussian distributions with differing means and standard deviations so that 
# they all have a mean of 0 and std of 1. This method works best with algorithms which assume Guassian distribution
# and work well with rescaled data e.g. linear regression, logistic regression and linear discriminate analysis

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler().fit(features) # fit features to std scaler
rescaled_features = scaler.transform(features) # apply transformation
print(rescaled_features[0:5,:]) # show output, all features now have guassian distribution

# c) Normalise Data (sklearn Normalizer)
# This method rescales each row (observation) to have values between 0 and 1 (a.k.a. a unit norm), this is useful for
# sparse data sets with lots of 0s or missing values when using weights or distance e.g. neural networks,
# K-nearest neighbours

from sklearn.preprocessing import Normalizer

scaler = Normalizer().fit(features)
normalized_features = scaler.transform(features)
print(normalized_features[0:5,:])

# d) Binarize Data (make binary)
# Here you set a threshold and if a value is above/below that threshold it's set to a 1/0 respectively. This can be
# useful for probabilities when you want a clear outcome.

from sklearn.preprocessing import Binarizer

binarizer = Binarizer(threshold = 0.0).fit(features)
binary_features = binarizer.transform(features)
print(binary_features[0:5,:])

############################################################################

# FEATURE SELECTION

# Irrelevant features in the data can have negative effects on the outcome of your model, there are 3 main reasons
# why automatic feature selection to remove irrelevant features is helpful:
    # Prevents overfitting - having less redundant data reduces chance of making decisions based on noise
    # Improves accuracy - having fewer outliers reduces error, particularly in linear processes e.g. regression
    # Reduces time - having fewer variables requires shorter processing times
    
# a) Univariate Selection
# This method selects the variables which have the greatest effect on the output class value, in this specific
# example chi-squared is used to find the best 4 non-negative features

from sklearn.feature_selection import SelectKBest, chi2

test = SelectKBest(score_func=chi2, k=4) # select 4 variables with strongest relationship to outputs using chi-squared
fit = test.fit(features, labels) # fit selection model on features and labels
print(fit.scores_) # print all scores
selected_features = fit.transform(features) # apply selection to extract 4 best variables
print(selected_features[0:5,:]) # show first 5 rows of 4 selected vars (plas, test, mass and age)

# b) Recursive Feature Elimination
# http://machinelearningmastery.com/feature-selection-machine-learning-python/
# continue from here!