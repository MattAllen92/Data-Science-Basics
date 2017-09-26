import numpy as np
from sklearn import preprocessing

############################################################################

# basic scaling

x = np.array([[1.,-1., 2.],
              [2., 0., 0.],
              [0., 1.,-1.]])

x_scaled = preprocessing.scale(x)  # scales the above data
x_scaled.mean(axis=0)              # scaling creates a mean of 0 for all vars
x_scaled.std(axis=0)               # it also creates a std of 1 for all vars

############################################################################            
            
# standard scaler (store scaling model for future application)

scaler = preprocessing.StandardScaler().fit(x)   # fit scaler to mean, std etc. of training data (x)
scaler.mean_                                     # stores the mean
scaler.scale_                                    # and the scale of the data
scaler.transform(x)                              # can then apply the model to any data

############################################################################                
                
# scaling features to a range (often between 0 and 1)

x_train = np.array([[1.,-1., 2.],
                    [2., 0., 0.],
                    [0., 1.,-1.]])

# create scaler between 0 and 1
min_max_scaler = preprocessing.MinMaxScaler()
x_train_minmax = min_max_scaler.fit_transform(x_train)
x_train_minmax

# apply above scaler to new data set, applying the same scaling and shifting
x_test = np.array([[-3.,-1., 4.],
                   [4., -4., 2.],
                   [3., 2., -2.]])
x_test_minmax = min_max_scaler.transform(x_test)
x_test_minmax

# you can check the properties of the scaler
min_max_scaler.scale_
min_max_scaler.min_

# Sparse Data:
# NOTE: MaxAbsScaler() is a similar scaler which uses a range of -1:1 instead of 0:1
# If you are dealing with standard data, the first methods (minMaxScaler) are best,
# however if you are using sparse data then you should either use maxAbsScaler because
# it will preserve the sparseness of the data OR you can use minMaxScaler/standardScaler
# but you must use scipy.sparse matrices and set with_mean=False

# Outliers in data:
# When there are outliers, using the above scaling methods are unlikely to work due to
# the fact that these use variance and mean. Therefore you should use robust_scale and
# RobustScaler, these use better methods to estimate the center and range of your data.

############################################################################

# normalize variables

x = [[1.,-1., 2.],
     [2., 0., 0.],
     [0., 1.,-1.]]

x_normalized = preprocessing.normalize(x, norm='l2') # normalizes single array dataset

normalizer = preprocessing.Normalizer().fit(x) # creates model to do the same as above
normalizer.transform(x) # you can then run the above model on any vector

# NOTE: if using sparse data, you must convert into compressed sparse rows using
# scipy.sparse.csr_matrix (see documentation).

############################################################################

# binarizing data

# in some cases you will need to convert numerical data into 0s and 1s depending
# on certain thresholds or criteria that you define.

x = [[ 1., -1.,  2.],
     [ 2.,  0.,  0.],
     [ 0.,  1., -1.]]

binarizer = preprocessing.Binarizer().fit(x) # fit does nothing, it's just a required step
binarizer.transform(x) # converts array to 0s and 1s

############################################################################

http://scikit-learn.org/stable/modules/preprocessing.html