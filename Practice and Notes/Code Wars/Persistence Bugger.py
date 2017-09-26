# my long winded way
def persistence(n):
    count = 0
    if len(str(n)) == 1:
        return count
    else:
        count += 1
        res = sum_mult(n)
        while len(str(res)) > 1:
            count += 1
            res = sum_mult(res)
        return count

def sum_mult(x):
    res = 1
    for num in str(x):
        res *= int(num)
    return res

print persistence(39)

# efficient way
import operator

def persistence2(n):
    count = 0
    while n >= 10:
        n = reduce(operator.mul, [int(x) for x in str(n)], 1)
        count += 1
    return count

print persistence(39)