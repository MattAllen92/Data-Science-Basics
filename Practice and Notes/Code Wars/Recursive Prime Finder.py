def nextPrime(n):
    nextVal = n+1
    if testPrime(nextVal) == -1:
        nextPrime(nextVal+1)
    else:
        return nextVal

def testPrime(x):
    a = 2
    while a < x:
        if x%a==0 and x!=a:
            return -1
        a += 1
    else:
        return x
    
print nextPrime(911)