# my long winded solution
def triple_double(num1, num2):
    triple = False
    double = False
    n1 = str(num1)
    n2 = str(num2)
    for i in range(2, len(n1)):
        if n1[i] == n1[i-1] == n1[i-2]:
            triple = True
    for j in range(2, len(n2)):
        if n2[j] == n2[j-1]:
            double = True
    if triple and double:
        return 1
    else:
        return 0
    
print triple_double(451999277, 41177722899)

# elegant solution
def trip_dub(n1, n2):
    return any([i*3 in str(n1) and i*2 in str(n2) for i in '0123456789'])
    
print trip_dub(451999277, 41177722899)