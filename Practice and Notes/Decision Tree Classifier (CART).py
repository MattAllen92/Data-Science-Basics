import pandas as pd
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn import datasets, metrics

# load data
dataset = datasets.load_iris() # load iris data from web                     
dataset.data # show features (as array of lists of 4 vars per row)
dataset.target # show labels (as array of 0, 1 or 2)

# fit model to data
model = DecisionTreeClassifier() # create CART object
model.fit(dataset.data, dataset.target) # fit model to features, labels
print(model) # show parameters of model

# predict
expected = dataset.target
predicted = model.predict(dataset.data)

# summarise output
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))

# THE ISSUE HERE IS THAT YOU ARE TRAINING AND TESTING THE MODEL ON THE SAME DATA
# NEED TO SPLIT IT, CROSS-VALIDATE AND CHECK ACCURACY ETC. THEN

##############################################################################

# new method to validate and not overfit:

#df = pd.DataFrame(dataset)
X = dataset.data # extract data into array/list with 150 elements, each containing 5 pieces of data (array of 150 rows x 5 cols)
Y = dataset.target
#X = array[:,0:4] # extract all rows for cols 1-4
#Y = array[:,4] # extract all rows for col 5
validation_size = 0.20 # define proportion of validation/test set
seed = 7 # starting point for pseudo-random sampling, ensure each random generation is comparable

# splits input data into train features (80%), test features (20%) and train labels (80%) and test labels (20%) respectively
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

# select best model and use for predictions

# KNN had the highest accuracy and lowest std (according to site, actually SVM did)
CART = DecisionTreeClassifier() # select KNN package to use
CART.fit(X_train, Y_train) # fit model to train data 
predictions = CART.predict(X_validation) # predict test data labels based on test features
print(accuracy_score(Y_validation, predictions)) # analyse accuracy (float of accuracy e.g. 0.9)
print(confusion_matrix(Y_validation, predictions)) # analyse confusion matrix
print(classification_report(Y_validation, predictions)) # analyse report