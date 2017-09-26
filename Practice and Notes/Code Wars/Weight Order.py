in1 = "2000 10003 1234000 44444444 9999 11 11 22 123"
#
#def order_weight(strng):
#    weight_score = {}
#    for weight in strng.split():
#        weight_score[weight] = sum([int(x) for x in str(weight)])
#    return sorted([x for x, y in weight_score.iteritems()], key=int)
#
#print order_weight(in1)
#
##weight = 103
##print sum([int(x) for x in str(weight)])

#def order_weight(strng):
#    wt_val = {}
#    output = []
#    for wt in strng.split():
#        val = sum(list(str(wt))
#        wt_val[wt] = val
#    for wt, val in wt_val.iteritems():
#        if output == []:
#            output.append(wt)
#        else:
#            for prev_wt in output:
#                if wt_val[prev_wt] > wt_val[wt]:
#                    output

#def order_weight(strng):
#    return [x for x in strng.split()]
#
#print order_weight(in1)

#wt = "102"
#print sum([int(x) for x in wt])
#strng = "103 123 4444 99 2000"
#test = {}
#test[strng.split()] = [sum(int(x) for x in wt) for wt in strng.split()]
#print test

#def order_weight(strng):
#    wt_val = {}
#    for wt in strng.split():
#        wt_val[wt] = sum([int(x) for x in wt])
#    return ' '.join([x[0] for x in sorted(wt_val.items(), key=lambda x: x[1])])
#
#print order_weight(in1)

def sum_string(s):
    return sum([int(x) for x in s])

def order_weight(strng):
    ordered = sorted(strng.split())
    return ' '.join(sorted(ordered, key=sum_string))

print order_weight(in1)