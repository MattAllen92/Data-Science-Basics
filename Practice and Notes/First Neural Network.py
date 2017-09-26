# http://iamtrask.github.io/2015/07/12/basic-python-network/

# Notes on the below code
# Sigmoid Functions - F(x)=(1/1+e^-x) 
# The sigmoid function produces a probability between 0 and 1 but instead of
# jumping between the two (like perceptrons do) it transitions smoothly. The
# probability it generates is the output of a node and it changes slowly with
# input. Therefore a small change in input could flip a perceptron entirely,
# however in a sigmoid neuron the change would have a proportional effect. To
# observe the effect of these small changes to output, you apply the sigmoid
# function to the dot product of the weights and bias to create a smooth
# overall output. Weights are initially randomly generated and then applied
# to inputs to create an output, the bias is added to the weight*input value
# therefore the higher the bias, the more likely the node output is to be 1
# (instead of 0) The reason the sigmoid function is chosen over other functions
# which produce smooth outputs is that exponential functions are all fairly similar
# and cheaper to handle computationally and since learning algorithms require
# lots of differentiation, this makes sense.
# Output = 1 if w.in + b > 0 OR 2 if w.in + b <= 0 (formula for perceptron node output)

# Setting the random seed
# When you set the seed for a random number, this number is multiplied by a
# very large number and then you take the modulo of this number to get the
# random number desired. By setting the seed each time you guarantee that you
# will generate the same set of numbers each time. This is done in ML because,
# for example, if you want to randomly split a training data set you will ensure
# that you split it the same way each time making the process reproducible and
# therefore directly comparable. When you set a seed it generates (pesudo)random
# numbers because even though the numbers have something done to them which
# we don't know about, the numbers returned are always the same if the seed is
# set. It's a way of ensuring consistency in random number generation.

# Derivatives
# READ UP ON DERIVATIVES!!! (link in the site at the top)

import numpy as np          # linear algebra library

# sigmoid function (maps values to a probability between 0 and 1)
def nonlin(x,deriv=False):  # define sigmoid function
    if(deriv==True):        # generates derivative of sigmoid (slope of the function at a given point)
        return x*(1-x)      # efficient way of calculating the derivative
    return 1/(1+np.exp(-x)) # otherwise calculate the sigmoid function of x
    
# input data
x = np.array([[0,0,1],
              [0,1,1],
              [1,0,1],
              [1,1,1]])     # create a multi-dimensional array (4 cols, 3 rows)

# output data
y = np.array([[0,0,1,1]]).T # .T transposes the array (swaps cols and rows)
                            # for a 1D array this does nothing...
                            
# set the seed (deterministic, reproducible)
np.random.seed(1) # set the seed at 1, integers fix the seed

# initialise weights randomly with mean 0
syn0 = 2*np.random.random((3,1)) - 1 # array (3r1c) of random numbers from -1 to 0 (i.e. last number subtracted)

for iter in xrange(10000):                # iterate 10000 times
    
    # forward propogation                 # sigmoid of input * weight -> output
    l0 = x                                # layer 1 of the network; input data
    l1 = nonlin(np.dot(l0,syn0))          # layer 2 of the network; hidden layer
                                          # or the smoothed output of x.w i.e. sigmoid(x.w)
    
    # calculate the error
    l1_error = y - l1                     # error = expected output - actual output
    
    # multiply error by slope of sigmoid
    l1_delta = l1_error * nonlin(l1,True) # I think this calculates gradient of descent

    # update the weights
    syn0 += np.dot(l0.T,l1_delta)         # current weight + (transposed inputs * gradient of descent)
    
print "Output After Training:"
print l1




    




