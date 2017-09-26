def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    output = []
    for num in range(a, b+1):
        if num == sum(int(x)**(i+1) for i, x in enumerate(str(num))):
            output.append(num)
    return output