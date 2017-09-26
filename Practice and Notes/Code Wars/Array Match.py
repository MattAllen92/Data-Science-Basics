a1 = ["live", "arp", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

#print [x in a2 for x in a1] # extract T/F for exact matches
#print sorted(set(a1) & set(a2)) # sort exact matches

# my long winded solution
def in_array(array1, array2):
    output = []
    for i in array1:
        for j in array2:
            if i in j and not i in output:
                output.append(i)
    return sorted(output)

print in_array(a1, a2)

# elegant solution
def in_array2(array1, array2):
    return sorted({sub for sub in a1 if any(sub in s for s in a2)})

print in_array2(a1, a2)