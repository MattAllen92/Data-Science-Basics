def my_crib(n):
    width = (n * 2) + 2
    roof = []
    house = []
    for i in range(1, n+1):
        roof_length = i*2 + 2
        house_length = n*2 + 2
        roof_buff = " " * int(buffer(width, roof_length))
        house_buff = " " * int(buffer(width, house_length))
        if roof == []:
            roof.append(roof_buff + " /\\ " + roof_buff)
        if i != n:
            roof.append(roof_buff + "/" + (" " * (i*2)) + "\\" + roof_buff)
            house.append(house_buff + "|" + (" " * (n*2)) + "|" + house_buff)
        elif i == n:
            roof.append(roof_buff + "/" + ("_" * (i*2)) + "\\" + roof_buff)
            house.append(house_buff + "|" + ("_" * (n*2)) + "|" + house_buff)
    crib = roof + house
    return '\n'.join(crib)
  
def buffer(w, l):
    return (w-l) / 2

print my_crib(1)