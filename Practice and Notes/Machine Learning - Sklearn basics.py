import numpy as np
from sklearn import tree
from sklearn.datasets import load_iris

def applesAndOranges():
    #train data
    features = [[140,1],[130,1],[150,0],[170,0]] #4 sets of 2 variable input data
    labels = [0,0,1,1] #4 known output values
    
    #classifier
    clf = tree.DecisionTreeClassifier() #create classifier (i.e. algorithm which finds patterns)
    clf = clf.fit(features,labels) #create model of relationships between inputs and outputs
    
    #test data prediction
    print clf.predict([[160,0]]) #use model to predict test input
    

def iris():
    iris = load_iris() #load data set
    test_idx = [0,50,100] #indexes for where each species starts (3 sets of 50 in a full set of 150)    
    
    #training data
    train_target = np.delete(iris.target, test_idx) #removes the three indexes 0, 50 and 100
    train_data = np.delete(iris.data, test_idx, axis=0) #removes the three indexes 0, 50 and 100
    
    #testing data
    test_target = iris.target[test_idx] #selects three indexes 0, 50 and 100
    test_data = iris.data[test_idx] #selects three indexes 0, 50 and 100
    
    #classifier
    clf = tree.DecisionTreeClassifier()
    clf.fit(train_data, train_target)
    
    print test_target #give it [0, 1, 2]
    print clf.predict(test_data) #predicts [0, 1, 2]
    
#    print iris.feature_names #show features (i.e. input variable labels)
#    print iris.target_names #show targets (i.e. output variable values)
#    print iris.data[0] #data for first item
#    print iris.target[0] #output for first item
    


#call methods
#applesAndOranges()
#iris()