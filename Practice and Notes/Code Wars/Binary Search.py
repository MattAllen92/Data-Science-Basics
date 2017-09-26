import time

# find the middle point, check value, search within valid half until you
# get the correct number

#def binary_search(x, y, n, count=1):
#    mid = (x + y) / 2
#    if mid < n:
#        binary_search(mid, y, n, count+1)
#        return
#    if mid > n:
#        binary_search(x, mid, n, count+1)
#        return
#    else:
#        print mid, count
#        return
#
#binary_search(1, 300, 37)

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79]

def binary_search_array(arr, n, count=1):
    minVal = 0
    maxVal = len(arr) - 1
    midVal = (minVal + maxVal) / 2
    if n not in primes:
        print "Your number is not a prime!"
        return
    if arr[midVal] == n:
        print ("Your number was %d" % arr[midVal]), count
        return
    if arr[midVal] < n:
        if midVal == 0:
            print ("Your number was %d" % arr[1]), count
            return
        else:
            binary_search_array(arr[midVal:], n, count+1)
            return
    if arr[midVal] > n:
        if midVal == 0:
            print ("Your number was %d" % arr[1]), count
            return
        else:
            binary_search_array(arr[:midVal], n, count+1)
            return    
    
start_time = time.time()

for prime in primes:
    binary_search_array(primes, prime)

print "--- %s seconds ---" % (time.time() - start_time)