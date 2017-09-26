def sum_pairs(ints, s):
    for x in ints:
        for y in range(ints.index(x)):
            if int(x) + int(ints[y]) == s:
                return [x, ints[y]]
    return None

print sum_pairs([11,3,7,5], 10)

ints = [11,3,7,5]

#print ints[2]
#print ints.index(11)
#print ints[2] + ints.index(11)