# 1) Generators
# standard iterator
def firstn(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums

output1 = firstn(10)

# generator
def firstn_gen(n):
    num = 0
    while num < n:
        yield num
        num += 1
        
output2 = firstn_gen(10)
list(output2)

# generator (list comprehension syntax)
firstn_genLC = list(i for i in xrange(10))

# after creating a generator, you can use it in 2 ways...
def gen1():
    yield 1
    yield 2
    
for i in gen1():
    print i

gen1_obj = gen1()   
next(gen1_obj)

# get primes example
# note: isPrime was taken off the internet
def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False    

    return True

def get_primes(n):
    num = 0
    while num < n:
        if isPrime(num):
            yield num
        num += 1
        
for i in get_primes(5):
    print i
    
# generators call next() when you iterate over them, if 'return' is encountered
# or you reach the end of the iterable then stopiteration() is called and the
# generator function is terminated
# therefore the while loop above ensures we never reach the end of the iterable

