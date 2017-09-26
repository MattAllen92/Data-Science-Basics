ex1 = [1,2,3] # false
ex2 = [-5,-3,-1,2,4,6] # false
ex3 = [-1,1] # true
ex4 = [-97364, -71561, -69336, 19675, 71561, 97863] # true

def subsetSum(x):
    for i in x:
        for j in x:
            if i + j == 0:
                return True
    else:
        return False
    
print subsetSum(ex1)
print subsetSum(ex2)
print subsetSum(ex3)
print subsetSum(ex4)