def is_twinprime(n):
    prime = is_prime(n)
    if prime == True:
        if is_prime(n-2) or is_prime(n+2):
            return True
        else:
            return False
    else:
        return False
        
def is_prime(x):
    for i in range(2,x+1):
        if x in [1,2,3]:
            return True
        elif x%i == 0 and x != i:
            return False
        elif x == i and x%i == 0:
            return True
    return False
    
print(is_twinprime(25))

print(is_prime(25))