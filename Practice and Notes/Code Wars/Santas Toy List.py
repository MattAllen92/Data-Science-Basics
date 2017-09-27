GIFTS = {
  1: 'Toy Soldier',
  2: 'Wooden Train',
  4: 'Hoop',
  8: 'Chess Board',
  16: 'Horse',
  32: 'Teddy',
  64: 'Lego',
  128: 'Football',
  256: 'Doll',
  512: "Rubik's Cube"
}

gifts_list = []

def gifts(num):
    while num > 0:
        val = get_values(num)
        toy = GIFTS[val]
        if toy not in gifts_list:
            gifts_list.append(toy)
        num -= val
    return sorted(gifts_list)
            
def get_values(num):
    values = sorted(list(GIFTS.keys()))
    for val in values:
        if val > num:
            prev = values[values.index(val) - 1]
            return prev
    
print gifts(2)