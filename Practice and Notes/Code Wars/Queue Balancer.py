def queue_time(customers, n):
    qn = [0] * n
    print qn
    for c in customers:
        print c
        qn = sorted(qn)
        print qn
        qn[0] += c
        print qn
    return max(qn)

print queue_time([1,4,3,10,2,6], 4)

# continuously sort the list and add the next customer time to the smallest
# value, once complete, return the maximum value which will tell you the
# time it takes to clear all customers.