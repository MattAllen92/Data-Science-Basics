def dig_pow(n, p):
    components = []
    for i in range(len(str(n))):
        num = int(str(n)[i])
        power = p + i
        components.append(num**power)
    output = sum(components)
    if output % n == 0:
        return output/n
    else:
        return -1
    
print dig_pow(46288,3)