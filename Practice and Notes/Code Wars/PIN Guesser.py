import itertools

adj_dict = {1:[1,2,4],2:[1,2,3,5],3:[2,3,6],4:[1,4,5,7],
            5:[2,4,5,6,8],6:[3,5,6,9],7:[4,7,8],
            8:[5,7,8,9,0],9:[6,8,9],0:[8,0]}

def get_pins(observed):
    observed_options = [adj_dict[int(x)] for x in str(observed)] # this creates an array of arrays for each possible code for the given code
    return [''.join(str(y) for y in x) for x in list(itertools.product(*observed_options))] # this produces all the different combinations of array items in the observed_options list

print get_pins(46)

#tup = (1,4)
#print ''.join([str(x) for x in tup])