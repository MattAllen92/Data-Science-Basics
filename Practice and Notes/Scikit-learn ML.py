# Python Scikit-learn tutorial
# incorporates multiple types of ML
# http://machinelearningmastery.com/machine-learning-in-python-step-by-step/

# libraries

# installing pandas, matplotlib and multiple scikit-learn packages for
# multiple machine learning methods to try out
import pandas
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

##############################################################################
##############################################################################
##############################################################################

# load dataset

# using iris data (i.e. the 'hello world' of ML)
#url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data" # csv data file (5 cols, 150 rows)
rawIrisData = r"C:\Users\AllenM\Desktop\TGI-Ops\MA Programs\Python Scripts\Practice and Notes\Iris Data (for ML)\iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(rawIrisData, names=names) # reads csv data into df with col names labelled as above
                         
##############################################################################
##############################################################################
##############################################################################

# examine the data set

##############################################################################

# statistical properties
print(dataset.shape) # (rows, cols)
print(dataset.head(20)) # first 20 rows
print(dataset.describe()) # count, mean, std, min etc. (per column)
print(dataset.groupby('class').size()) # group by column 'class' (i.e. species) and show amount of each

##############################################################################

# visualization

# univariate (individual variables)
# box and whisker plot, each in distinct graphs, 2x2 grid presentation, each with their own scale (i.e. sensible range)
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()
# histograms
dataset.hist()
plt.show() # potentially gaussian distribution between some variables (i.e. normal distribution)

# multivariate
# scatter plot matrix
scatter_matrix(dataset) # compares every variable against each other in a grid
plt.show() # some variables appear to have a high correlation/predictable relationship

##############################################################################
##############################################################################
##############################################################################

# evaluate some algorithms

# stages:
# 1) separate out validation dataset (80:20 train:validation)
# 2) set up test harness to use 10-fold cross validation
# 3) build 5 different models to predict species from data
# 4) select the best model

##############################################################################
    
# 1) isolate validation dataset
    
array = dataset.values # extract data into array/list with 150 elements, each containing 5 pieces of data (array of 150 rows x 5 cols)
X = array[:,0:4] # extract all rows for cols 1-4
Y = array[:,4] # extract all rows for col 5
validation_size = 0.20 # define proportion of validation/test set
seed = 7 # starting point for pseudo-random sampling, ensure each random generation is comparable

# splits input data into train features (80%), test features (20%) and train labels (80%) and test labels (20%) respectively
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

##############################################################################

# 2) test harness (10-fold cross validation)
    
# aim: split data into 10 parts, train on 9, test on 1 and repeat for all combos
seed = 7 # starting point for pseudo-random sampling
scoring = 'accuracy' # this setting calculates ratio of correctly predicted cases from total sample as a %

# the data set looks like there is some correlation between variables so the output should be good
# however, we don't know the best ML model to use yet, so we will build and evaluate 5 different ones

# simple linear:
# logistic regression (LR)
# linear discriminant analysis (LDA)

# non-linear:
# k-nearest neighbours (KNN)
# classification and regression trees (CART)
# gaussian naive bayes (NB)
# support vector machines (SVM)

# reset seed before each run to ensure each algorithm evaluation is peformed
# using identical data splits (i.e. directly comparable)

# build models
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC())) # create list containing each model

# evaluate each model in turn
results = []
names = [] # will create lists of accuracies for each model above
for name, model in models: # iterate through models, assigning name and model (e.g. LR:LogisticRegression())
    kfold = model_selection.KFold(n_splits=10, random_state=seed) # define kfold with 10 splits and 7 as the seed
    # cross-validate each model against the same train and test data, cv defines which cross validation, scoring is 'accuracy' from above
    cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
    results.append(cv_results) # record accuracy score for model (list of accuracies, 10 per model)
    names.append(name) # record which model the accuracy has been generated for
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())  # prints name: mean accuracy, std accuracy
    print(msg) # the higher the mean and the lower the std the better -> SVM looks pretty good!
    
# compare the algorithms (visualization)
fig = plt.figure() # create figure instance
fig.suptitle('Algorithm Comparison') # grid title
ax = fig.add_subplot(111) # 1x1 grid
plt.boxplot(results) #  10 accuracy scores per model used
ax.set_xticklabels(names) # x axis = model names
plt.show() # show box and whisker graph

##############################################################################
##############################################################################
##############################################################################

# select best model and use for predictions

# KNN had the highest accuracy and lowest std (according to site, actually SVM did)
knn = KNeighborsClassifier() # select KNN package to use
knn.fit(X_train, Y_train) # fit model to train data 
predictions = knn.predict(X_validation) # predict test data labels based on test features
print(accuracy_score(Y_validation, predictions)) # analyse accuracy (float of accuracy e.g. 0.9)
print(confusion_matrix(Y_validation, predictions)) # analyse confusion matrix
print(classification_report(Y_validation, predictions)) # analyse report